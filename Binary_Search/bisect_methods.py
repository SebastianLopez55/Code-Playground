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


if __name__ == "__main__":

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
