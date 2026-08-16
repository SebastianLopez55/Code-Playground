from typing import Callable, List


class bisect:
    """Binary-search utilities operating on ascending-sorted sequences."""

    @staticmethod
    def _bisect(arr: List[int], target: int, comparator: Callable[[int, int], bool]) -> int:
        """
        Shared half-open binary search core for bisect_left / bisect_right.

        `comparator(arr[mid], target)` decides whether `mid` stays left of
        the answer: `<` gives bisect_left, `<=` gives bisect_right.

        O(log n) time
        O(1) auxiliary space
        O(n) total space
        """
        left, right = 0, len(arr)      # half-open [left, right), right is always excluded

        while left < right:            # stops when search space [left, right) is empty
            mid = left + ((right - left) // 2)

            if comparator(arr[mid], target):
                left = mid + 1
            else:
                right = mid

        return left

    @staticmethod
    def bisect_left(arr: List[int], target: int) -> int:
        """
        Leftmost insertion point for `target` in `arr`: the index of the
        first element >= target. If `target` is present, this is the
        index of its leftmost occurrence.

        O(log n) time
        O(1) auxiliary space
        O(n) total space
        """
        return bisect._bisect(arr, target, lambda a, b: a < b)

    @staticmethod
    def bisect_right(arr: List[int], target: int) -> int:
        """
        Rightmost insertion point for `target` in `arr`: the index of the
        first element > target. If `target` is present, this is one past
        the index of its rightmost occurrence.

        O(log n) time
        O(1) auxiliary space
        O(n) total space
        """
        return bisect._bisect(arr, target, lambda a, b: a <= b)

    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """
        Classic binary search, built on bisect_right: returns the index
        of `target` in `arr`, or -1 if it is not present.

        O(log n) time
        O(1) auxiliary space
        O(n) total space
        """
        index = bisect.bisect_right(arr, target)

        if index > 0 and arr[index - 1] == target:
            return index - 1
        return -1

    @staticmethod
    def binary_search_on_answer(lo: int, hi: int, condition: Callable[[int], bool]) -> int:
        """
        Binary search over an abstract answer space [lo, hi] instead of
        over an array -- the "find the min X such that condition(X) is
        true" pattern.

        `condition` must be monotonic across [lo, hi]: False for every
        value below the answer, True for the answer and everything above
        it (F F F ... F T T T ... T). Never write a condition that flips
        back to False after becoming True -- the search assumes it can't.

        `hi` must already be a value you know satisfies condition(hi) is
        True (e.g. the largest legal answer to the problem). The loop
        narrows toward `hi` but never calls condition(hi) itself, the
        same way bisect_left/_bisect never index arr[len(arr)] -- `hi`
        plays the role of that one-past-the-end sentinel.

        Structurally this is arr[mid] < target from _bisect with
        arr[mid] swapped for condition(mid): same half-open [l, r) loop,
        same "move right past a mid that fails, else pull left down to
        it" logic.

        O(log(hi - lo)) iterations, each paying whatever condition(x) costs
        O(1) auxiliary space
        """
        l, r = lo, hi              # half-open [l, r); r is a known-True sentinel, never tested

        while l < r:                # stops when search space [l, r) is empty
            mid = l + ((r - l) // 2)

            if condition(mid):       # mid works -- answer is mid or something smaller
                r = mid
            else:                    # mid fails -- answer must be larger than mid
                l = mid + 1

        return l


if __name__ == "__main__":

    # ------------------------------------------------------------------
    # bisect_left / bisect_right / binary_search -- array-based searches
    # ------------------------------------------------------------------

    nums = [1, 2, 3, 4, 4, 4, 4, 5]
    print(nums)

    print(f"bisect_left(nums, 4)  -> {bisect.bisect_left(nums, 4)}")
    print(f"bisect_right(nums, 4) -> {bisect.bisect_right(nums, 4)}")
    print(f"count of 4s in nums   -> {bisect.bisect_right(nums, 4) - bisect.bisect_left(nums, 4)}")

    print(f"bisect_left(nums, 7)  -> {bisect.bisect_left(nums, 7)}")
    print(f"bisect_right(nums, 7) -> {bisect.bisect_right(nums, 7)}")
    print(f"count of 7s in nums   -> {bisect.bisect_right(nums, 7) - bisect.bisect_left(nums, 7)}")

    print(f"binary_search(nums, 3) -> {bisect.binary_search(nums, 3)}")
    print(f"binary_search(nums, 7) -> {bisect.binary_search(nums, 7)}")

    # ------------------------------------------------------------------
    # binary_search_on_answer -- condition-based searches over a value
    # range instead of an array
    # ------------------------------------------------------------------

    # Scenario 1: smallest x such that x*x >= n  (ceiling of sqrt(n))
    # condition(x) is False for every x with x*x < n, then flips True and
    # stays True -- exactly the monotonic shape the search requires.
    n = 17
    smallest_x_squared_geq_n = bisect.binary_search_on_answer(
        lo=0, hi=n, condition=lambda x: x * x >= n
    )
    print(f"smallest x with x^2 >= {n} -> {smallest_x_squared_geq_n}  (check: {smallest_x_squared_geq_n ** 2} >= {n})")

    # Scenario 2: Koko Eating Bananas (LeetCode 875)
    # Find the minimum eating speed k such that Koko can finish every
    # pile within h hours. condition(k) is False for speeds too slow to
    # finish in time, True once k is fast enough -- and stays True for
    # every faster speed, so it's monotonic.
    piles = [3, 6, 7, 11]
    h = 8

    def hours_needed(speed: int) -> int:
        return sum(-(-pile // speed) for pile in piles)  # ceil division without importing math

    min_eating_speed = bisect.binary_search_on_answer(
        lo=1, hi=max(piles), condition=lambda speed: hours_needed(speed) <= h
    )
    print(f"min eating speed for piles={piles}, h={h} -> {min_eating_speed}  (hours needed: {hours_needed(min_eating_speed)})")
