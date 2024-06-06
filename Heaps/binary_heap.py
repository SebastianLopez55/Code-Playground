from operator import index
from typing import List

from distutils.command import build


class MinHeap:
    def __init__(self) -> None:
        self.size = 0
        self.items = []

    def print_heap(self):
        print(self.items)

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

    def get_min(self):
        if self.size == 0:
            raise LookupError()
        return self.items[0]

    def extract_min(self):
        if self.size == 0:
            raise LookupError()
        min_item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self._bubble_down()
        return min_item

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self._bubble_up()

    def _bubble_down(self):
        pass

    def _bubble_up(self):
        item_idx = self.size - 1
        while (
            self.has_parent(item_idx) and self.parent(item_idx) > self.items[item_idx]
        ):
            self._swap(self.get_parent_idx(item_idx), item_idx)
            item_idx = self.get_parent_idx(item_idx)


# Example usage
min_heap = MinHeap()
