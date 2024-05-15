# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node is None:
                return

            path.append(str(node.val))

            if not node.left and not node.right:  # if reach a leaf
                paths.append("->".join(path))  # add path to result
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()  # backtrack to explore other paths

        dfs(root, [])
        return paths

    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # if reach a leaf
                    paths.append(path)  # add path to result
                else:
                    path += "->"  # extend the current path
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return paths


# Create a small binary tree
#       1
#      / \
#     2   3
#      \
#       5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

# Instantiate the solution class
solution = Solution()

# Test the functions
paths1 = solution.binaryTreePaths1(root)
paths2 = solution.binaryTreePaths2(root)

print("Paths from binaryTreePaths1:", paths1)
print("Paths from binaryTreePaths2:", paths2)
