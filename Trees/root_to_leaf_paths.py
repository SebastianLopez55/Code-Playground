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


def sum_paths_containing_target1(root, target):
    all_paths = []

    def preorder_dfs(root, path):
        if root is None:
            return

        path.append(root.val)

        if not root.left and not root.right:
            all_paths.append(list(path))

        if root.left:
            preorder_dfs(root.left, path)

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


def sum_paths_containing_target2(root, target):
    def dfs(node, current_path, current_sum, target, result):
        if not node:
            return

        # Add the current node's value to the path and sum
        current_path.append(node.val)
        current_sum += node.val

        # If it's a leaf node
        if not node.left and not node.right:
            # If the current path contains the target, add the sum to the result
            if target in current_path:
                result[0] += current_sum

        # Continue to traverse the left and right subtrees
        dfs(node.left, current_path, current_sum, target, result)
        dfs(node.right, current_path, current_sum, target, result)

        # Backtrack: remove the current node's value from the path and sum
        current_path.pop()
        current_sum -= node.val

    result = [0]
    dfs(root, [], 0, target, result)
    return result[0]


def sum_paths_containing_target3(root, target):
    def dfs(node, current_sum, target_found):
        if not node:
            return 0

        # Update the current path sum
        current_sum += node.val

        # Check if the target value is in the current path
        if node.val == target:
            target_found = True

        # If we reached a leaf node, check if target was found in the path
        if not node.left and not node.right:
            return current_sum if target_found else 0

        # Recur for left and right subtrees
        left_sum = dfs(node.left, current_sum, target_found)
        right_sum = dfs(node.right, current_sum, target_found)

        # Return the sum of valid paths from both subtrees
        return left_sum + right_sum

    # Start DFS from the root node
    return dfs(root, 0, False)


assert sum_paths_containing_target3(tree1, 0) == 11, "Failed test 1."
assert sum_paths_containing_target3(tree1, 5) == 6, "Failed test 2."
assert sum_paths_containing_target3(tree1, 1) == 15, "Failed test 3."

print("All tests passed!")
