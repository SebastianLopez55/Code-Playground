from typing import Optional, Tuple


# Definition for a binary tree node
class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


def find_kth_max(root: Optional[TreeNode], k: int) -> int:
    def reverse_inorder_traversal(
        node: Optional[TreeNode], k: int
    ) -> Tuple[int, Optional[int]]:
        # Base case: if the node is None, return count as 0 and value as None
        if not node:
            return 0, None

        # Visit the right subtree first (larger values)
        count_right, value_right = reverse_inorder_traversal(node.right, k)

        # If we found the kth largest in the right subtree, return it
        if value_right is not None:
            return count_right, value_right

        # Count this node
        current_count = count_right + 1
        if current_count == k:
            return current_count, node.data

        # Visit the left subtree (smaller values)
        count_left, value_left = reverse_inorder_traversal(node.left, k - current_count)
        total_count = current_count + count_left
        return total_count, value_left

    # Start the reverse in-order traversal from the root
    _, result = reverse_inorder_traversal(root, k)
    return result if result is not None else 0


# Example usage:
# Constructing the BST
#         5
#        / \
#       3   8
#      / \ / \
#     2  4 7  9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

k = 3
print(f"The {k}rd maximum value in the BST is: {find_kth_max(root, k)}")
# Output should be 7
