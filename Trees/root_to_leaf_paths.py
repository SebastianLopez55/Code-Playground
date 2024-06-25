"""
Given a binary tree, return the sum of all root-to-leaf paths that contain a specified target value.
    
    Example:
    Tree:
         1
        / \
       0   3
      / \   
     4   5
    
Input: root, target = 0
Output: Sum of all root-to-leaf paths containing 0 = (1 + 0 + 4) + (1 + 0 + 5) = 11

Input: root, target = 5
Output: Sum of all root-to-leaf paths containing 5 = (1 + 0 + 5) = 6

Input: root, target = 1
Output: Sum of all root-to-leaf paths containing 1 = (1 + 0 + 4) + (1 + 0 + 5) + (1 + 3) = 15

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree1 = TreeNode(1, TreeNode(0, TreeNode(4), TreeNode(5)), TreeNode(3))


def paths_with_target(root, target):

    all_paths = []

    def preorder_dfs(root, path):
        if root is None:
            return

        if not root.left and not root.right:
            all_paths.append(path + [root.val])

        path.append(root.val)

        if root.left:
            preorder_dfs(root.left, path)
            path.pop()

        if root.right:
            preorder_dfs(root.right, path)
            path.pop()

    preorder_dfs(root, [])

    total_sum = 0
    for path in all_paths:
        path_set = set(path)
        if target in path_set:
            total_sum += sum(path)

    return total_sum


print(paths_with_target(tree1, 0))
