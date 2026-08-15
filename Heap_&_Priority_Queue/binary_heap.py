from typing import List
import random


class MinHeap:
    def __init__(self) -> None:
        self._size = 0
        self._items = []

    def print_heap(self) -> None:
        print(f"Current state of the Min Heap: {self._items}")

    def is_empty(self) -> bool:
        return self._size == 0

    def get_left_child_idx(self, parent_idx: int) -> int:
        left_child_idx = 2 * parent_idx + 1
        if left_child_idx >= self._size:
            raise IndexError("Left child index is out of bounds")
        return left_child_idx

    def get_right_child_idx(self, parent_idx: int) -> int:
        right_child_idx = 2 * parent_idx + 2
        if right_child_idx >= self._size:
            raise IndexError("Right child index is out of bounds")
        return right_child_idx

    def get_parent_idx(self, child_idx: int) -> int:
        if child_idx <= 0 or child_idx >= self._size:
            raise IndexError("Child index is out of bounds")
        parent_idx = (child_idx - 1) // 2
        return parent_idx

    def has_left_child(self, idx: int) -> bool:
        return 2 * idx + 1 < self._size

    def has_right_child(self, idx: int) -> bool:
        return 2 * idx + 2 < self._size

    def has_parent(self, idx: int) -> bool:
        return (idx - 1) // 2 >= 0

    def left_child(self, idx: int) -> int:
        return self._items[self.get_left_child_idx(idx)]

    def right_child(self, idx: int) -> int:
        return self._items[self.get_right_child_idx(idx)]

    def parent(self, idx: int) -> int:
        return self._items[self.get_parent_idx(idx)]

    def _swap(self, idx_one: int, idx_two: int) -> None:
        self._items[idx_one], self._items[idx_two] = (
            self._items[idx_two],
            self._items[idx_one],
        )

    def get_min(self) -> int:
        if self._size == 0:
            raise LookupError("Heap is empty")
        return self._items[0]

    def extract_min(self) -> int:
        if self._size == 0:
            raise LookupError("Heap is empty")
        min_item = self._items[0]
        self._items[0] = self._items[self._size - 1]
        self._size -= 1
        self._bubble_down(0)
        return min_item

    def insert(self, item: int) -> None:
        self._items.append(item)
        self._size += 1
        self._bubble_up()

    def _bubble_down(self, index: int) -> None:
        item_idx = index
        while self.has_left_child(item_idx):
            smaller_child_idx = self.get_left_child_idx(item_idx)
            if self.has_right_child(item_idx) and self.right_child(
                item_idx
            ) < self.left_child(item_idx):
                smaller_child_idx = self.get_right_child_idx(item_idx)

            if self._items[item_idx] < self._items[smaller_child_idx]:
                break
            else:
                self._swap(item_idx, smaller_child_idx)
                item_idx = smaller_child_idx

    def _bubble_up(self) -> None:
        item_idx = self._size - 1
        while (
            self.has_parent(item_idx) and self.parent(item_idx) > self._items[item_idx]
        ):
            self._swap(self.get_parent_idx(item_idx), item_idx)
            item_idx = self.get_parent_idx(item_idx)

    def heapify(self, array: List[int]) -> None:
        self._items = array
        self._size = len(array)
        # Start from the last non-leaf node and go up to the root
        for i in range(self._size // 2 - 1, -1, -1):
            self._bubble_down(i)


# Example usage
min_heap = MinHeap()
random_array = [random.randint(1, 100) for _ in range(10)]
print(f"Random array: {random_array}")
min_heap.heapify(random_array)
min_heap.print_heap()
