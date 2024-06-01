# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_nodes = []
        self.node_idx = -1
        self._inorder_dfs(root)

    def _inorder_dfs(self, node):
        if not node:
            return

        self._inorder_dfs(node.left)
        self.inorder_nodes.append(node.val)
        self._inorder_dfs(node.right)

    def next(self) -> int:
        if self.hasNext():
            self.node_idx += 1
            return self.inorder_nodes[self.node_idx]
        else:
            raise StopIteration("No more elements in the iterator")

    def hasNext(self) -> bool:
        return self.node_idx + 1 < len(self.inorder_nodes)


# Helper function to insert nodes into the BST
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


# Create a test BST
root = TreeNode(7)
root = insert_into_bst(root, 3)
root = insert_into_bst(root, 15)
root = insert_into_bst(root, 9)
root = insert_into_bst(root, 20)

# Initialize the BSTIterator with the root
iterator = BSTIterator(root)

# Use the iterator to print elements in in-order sequence
while iterator.hasNext():
    print(iterator.next())

print(iterator.hasNext())
print(iterator.next())
