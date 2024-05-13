# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(
    7,
    TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)),
    TreeNode(9, TreeNode(8, None, None), TreeNode(10, None, None)),
)


# Inorder Traversal
def inorder_dfs(root):
    if root is None:
        return
    inorder_dfs(root.left)
    print(root.val)
    inorder_dfs(root.right)


inorder_dfs(tree)
