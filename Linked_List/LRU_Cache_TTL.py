import threading
import time


class LRUCache:
    """
    HashMap + doubly linked list, with a TTL on every entry (thread safe)

    The map gives O(1) key lookup straight to a node. The doubly linked list
    keeps nodes ordered by recency: the least_used sentinel sits on the left,
    the most_used sentinel on the right, and real nodes live between them.
    Nodes nearest most_used are the freshest.

    Doubly linked rather than singly so _remove can unlink a node in O(1)
    without scanning for its predecessor. The two sentinels mean insert and
    remove never touch a None pointer, so there are no head/tail edge cases.

    Two independent eviction rules:
      - capacity -> the least recently used entry is dropped on overflow
      - TTL      -> an entry is dead once the clock passes its expires_at

    Expiry is lazy: a dead entry keeps its slot until a read touches it, at
    which point get() unlinks it and reports a miss. Nothing scans the cache
    on a timer, so both operations stay O(1).

    Deadlines use time.monotonic(), which never runs backward. A wall clock
    like time.time() can jump (NTP, DST, manual changes) and silently extend
    or kill every deadline at once.

    get / put: O(1) time
    O(capacity) auxiliary space -> map plus one node per entry
    O(capacity) total space
    """

    class ListNode:
        def __init__(self, key, val, ttl, prev=None, next=None):
            self.key = key  # stored so eviction can delete the map entry
            self.val = val
            # absolute deadline, fixed at write time -- a slow reader can
            # never extend an entry's life
            self.expires_at = time.monotonic() + ttl
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int, ttl: float):
        self.capacity = capacity
        self.ttl = ttl  # seconds every entry lives after it is written
        self.cache = dict()

        # sentinels: least_used <-> most_used, real nodes inserted between
        self.least_used = self.ListNode(-1, -1, ttl)
        self.most_used = self.ListNode(-1, -1, ttl)
        self.least_used.next = self.most_used
        self.most_used.prev = self.least_used
        self._lock = threading.Lock()

    def get(self, key: int) -> int:
        with self._lock:
            if key not in self.cache:
                return -1

            node = self.cache[key]

            # dead entries are dropped rather than returned, so a caller can
            # never observe a value past its TTL
            if time.monotonic() > node.expires_at:
                self._remove(node)
                del self.cache[key]
                return -1

            # unlink and reinsert at the most-used end to refresh recency.
            # note this refreshes LRU order only -- reads never extend the TTL
            self._remove(node)
            self._insert(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        with self._lock:
            # drop the old node if the key is already present
            if key in self.cache:
                self._remove(self.cache[key])

            new_node = self.ListNode(key, value, self.ttl)  # fresh deadline
            self.cache[key] = new_node
            self._insert(new_node)

            # over capacity: evict the node beside the least_used sentinel
            if len(self.cache) > self.capacity:
                node_to_delete = self.least_used.next
                self._remove(node_to_delete)
                del self.cache[node_to_delete.key]

    def _insert(self, node):
        """Link node just before the most_used sentinel."""
        prev_to_most = self.most_used.prev
        prev_to_most.next = node
        node.prev = prev_to_most
        node.next = self.most_used
        self.most_used.prev = node

    def _remove(self, node):
        """Unlink node from the list in O(1)."""
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == "__main__":

    # TTL tests use short real sleeps. LONG_TTL is for the pure-LRU tests,
    # big enough that nothing expires mid-test.
    LONG_TTL = 60

    # ------------------------------------------------------------------
    # basic get/put round trip
    # ------------------------------------------------------------------

    cache = LRUCache(2, LONG_TTL)
    assert cache.get(1) == -1, "missing key should return -1"

    cache.put(1, 100)
    assert cache.get(1) == 100, "put then get should round-trip the value"

    # ------------------------------------------------------------------
    # put on an existing key overwrites the value, not the entry count
    # ------------------------------------------------------------------

    cache.put(1, 200)
    assert cache.get(1) == 200, "put on an existing key should overwrite its value"
    assert len(cache.cache) == 1, "overwriting a key must not grow the cache"

    # ------------------------------------------------------------------
    # eviction removes the least recently used entry once over capacity
    # ------------------------------------------------------------------

    cache = LRUCache(2, LONG_TTL)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # capacity exceeded -> evicts 1, the least recently used
    assert cache.get(1) == -1, "least recently used key should be evicted"
    assert cache.get(2) == 2
    assert cache.get(3) == 3

    # ------------------------------------------------------------------
    # get refreshes recency, saving a key from eviction
    # ------------------------------------------------------------------

    cache = LRUCache(2, LONG_TTL)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      # touch 1 -> 2 is now the least recently used
    cache.put(3, 3)   # evicts 2, not 1
    assert cache.get(2) == -1, "get(1) should have protected key 1 from eviction"
    assert cache.get(1) == 1
    assert cache.get(3) == 3

    # ------------------------------------------------------------------
    # put on an existing key also refreshes recency
    # ------------------------------------------------------------------

    cache = LRUCache(2, LONG_TTL)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # touch 1 -> 2 is now the least recently used
    cache.put(3, 3)   # evicts 2, not 1
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 3

    # ------------------------------------------------------------------
    # capacity of 1 keeps only the most recent key
    # ------------------------------------------------------------------

    cache = LRUCache(1, LONG_TTL)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # ------------------------------------------------------------------
    # the cache never grows past capacity, regardless of how many puts
    # ------------------------------------------------------------------

    cache = LRUCache(3, LONG_TTL)
    for key in range(10):
        cache.put(key, key)
    assert len(cache.cache) == 3
    for key in (7, 8, 9):  # only the last 3 inserted keys should remain
        assert cache.get(key) == key

    # ------------------------------------------------------------------
    # TTL: an entry dies once the clock passes its deadline
    # ------------------------------------------------------------------

    cache = LRUCache(10, ttl=0.05)
    cache.put(1, 1)
    assert cache.get(1) == 1, "entry should be alive well before its TTL"

    time.sleep(0.06)
    assert cache.get(1) == -1, "entry should be dead once past expires_at"

    # ------------------------------------------------------------------
    # TTL: reading a dead entry deletes it, freeing the slot
    # ------------------------------------------------------------------

    cache = LRUCache(10, ttl=0.05)
    cache.put(1, 1)
    time.sleep(0.06)
    assert len(cache.cache) == 1, "expiry is lazy -- the slot is held until touched"
    cache.get(1)
    assert len(cache.cache) == 0, "a failed get should drop the dead entry"

    # ------------------------------------------------------------------
    # TTL: re-putting a key resets its deadline
    # ------------------------------------------------------------------

    cache = LRUCache(10, ttl=0.1)
    cache.put(1, 1)
    time.sleep(0.07)
    cache.put(1, 2)   # fresh deadline from now
    time.sleep(0.07)  # 0.14s since the first put, only 0.07s since the second
    assert cache.get(1) == 2, "put should reset the TTL, not inherit the old one"

    # ------------------------------------------------------------------
    # TTL: get does NOT extend the deadline (recency != freshness)
    # ------------------------------------------------------------------

    cache = LRUCache(10, ttl=0.1)
    cache.put(1, 1)
    time.sleep(0.07)
    assert cache.get(1) == 1  # touching it refreshes LRU order only
    time.sleep(0.07)
    assert cache.get(1) == -1, "reads must not extend an entry's TTL"

    # ------------------------------------------------------------------
    # TTL entries still obey capacity eviction
    # ------------------------------------------------------------------

    cache = LRUCache(2, LONG_TTL)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == -1, "capacity eviction applies even to unexpired entries"
    assert len(cache.cache) == 2

    print("all LRUCache test cases passed")
