from typing import List


class MinHeap:
    def __init__(self) -> None:
        self.size = 0
        self.items = []

    def is_empty(self):
        return self.size == 0

    def get_left_child_idx(self, parent_idx):
        left_child_idx = 2 * parent_idx + 1
        if left_child_idx >= self.size:
            raise IndexError("Left child index is out of bounds")
        return left_child_idx

    def get_right_child_idx(self, parent_idx):
        right_child_idx = 2 * parent_idx + 2
        if right_child_idx >= self.size:
            raise IndexError("Right child index is out of bounds")
        return right_child_idx

    def get_parent_idx(self, child_idx):
        if child_idx <= 0 or child_idx >= self.size:
            raise IndexError("Child index is out of bounds")
        parent_idx = (child_idx - 1) // 2
        return parent_idx

    def has_left_child(self, idx):
        try:
            self.get_left_child_idx(idx)
            return True
        except IndexError:
            return False

    def has_right_child(self, idx):
        try:
            self.get_right_child_idx(idx)
            return True
        except IndexError:
            return False

    def has_parent(self, idx):
        try:
            self.get_parent_idx(idx)
            return True
        except IndexError:
            return False

    def left_child(self, idx):
        return self.items[self.get_left_child_idx(idx)]

    def right_child(self, idx):
        return self.items[self.get_right_child_idx(idx)]

    def parent(self, idx):
        return self.items[self.get_parent_idx(idx)]

    def _swap(self, idx_one, idx_two):
        self.items[idx_one], self.items[idx_two] = (
            self.items[idx_two],
            self.items[idx_one],
        )


# Example usage
min_heap = MinHeap()
