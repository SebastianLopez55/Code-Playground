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

    # O(n) time.
    # O(n) space.


# Morris Traversal: Inorder constant space tree traversal.
def morris_inorder(root):
    current = root
    while current:
        if current.left is None:

            # ======= Process Node ======
            print(current.val)
            # ===== Process Finished ====

            current = current.right
        else:
            # Find inorder predecessor of current.
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            if pre.right is None:
                # Make current as the right child of its inorder predecessor.
                pre.right = current
                current = current.left
            else:
                # Revert changes made in tree.
                pre.right = None

                # ======= Process Node ======
                print(current.val)
                # ===== Process Finished ====

                current = current.right

    # O(n) time.
    # O(1) space.


morris_inorder(tree)
