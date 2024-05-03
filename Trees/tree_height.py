class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    # Recursive DFS
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Creating nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

# Connecting nodes
node1.left = node2
node1.left = node3

# Now pass the root of the tree (node1) to the maxDepth function
depth = maxDepth(node1)
print("The maximum depth of the binary tree is:", depth)
