from itertools import zip_longest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def leaves(node, label):
            if node is None:
                return

            if node.left is None and node.right is None:
                print(f"    [{label}] generator woke up, yielding leaf {node.val}, now frozen")
                yield node.val
                return

            yield from leaves(node.left, label)
            yield from leaves(node.right, label)

        print("\n=== building the generators (nothing runs yet) ===")
        gen1 = leaves(root1, "tree1")
        gen2 = leaves(root2, "tree2")
        print(f"  gen1 = {gen1}")
        print(f"  gen2 = {gen2}")
        print("  no leaves visited yet, both are paused at line one")

        pairs = zip_longest(gen1, gen2, fillvalue=None)
        print(f"\n  pairs = {pairs}")
        print("  still nothing computed, zip_longest is also lazy")

        comparisons = (a == b for a, b in pairs)
        print(f"  comparisons = {comparisons}")
        print("  a generator expression, also paused")

        input("\n>>> press Enter to let all() start pulling values <<<")

        step = 1
        result = True

        while True:
            print(f"\n--- all() requests boolean #{step} ---")

            try:
                verdict = next(comparisons)
            except StopIteration:
                print("    both generators exhausted, no more pairs")
                print(f"\n=== all() consumed everything without a False -> {result} ===")
                break

            print(f"    comparison #{step} evaluated to {verdict}")

            if not verdict:
                result = False
                print(f"\n=== all() saw False and stopped immediately ===")
                print("    both tree traversals stay frozen and never resume")
                print(f"    any remaining leaves are NEVER visited -> {result}")
                break

            step += 1
            input(">>> press Enter for the next pair <<<")

        return result


# ---------------------------------------------------------------------------
#   tree1              tree2
#
#     1                  9
#    / \                / \
#   2   3              2   3
#
#  leaves: 2, 3       leaves: 2, 3        -> True
# ---------------------------------------------------------------------------
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(9, TreeNode(2), TreeNode(3))

# ---------------------------------------------------------------------------
#   tree3              tree4
#
#     1                  1
#    / \                / \
#   2   3              2   9
#      / \                / \
#     4   5              4   5
#
#  leaves: 2, 4, 5    leaves: 2, 4, 5     -> True, but watch the depths differ
# ---------------------------------------------------------------------------
tree3 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
tree4 = TreeNode(1, TreeNode(2), TreeNode(9, TreeNode(4), TreeNode(5)))

# ---------------------------------------------------------------------------
#   tree5              tree6
#
#     1                  1
#    / \                / \
#   2   3              2   9
#      / \                / \
#     4   5              7   5
#
#  leaves: 2, 4, 5    leaves: 2, 7, 5     -> False at the SECOND pair
#                                            the 5s are never reached
# ---------------------------------------------------------------------------
tree5 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
tree6 = TreeNode(1, TreeNode(2), TreeNode(9, TreeNode(7), TreeNode(5)))


if __name__ == "__main__":
    s = Solution()

    print("#" * 70)
    print("CASE 1 — matching leaves 2,3 vs 2,3")
    print("#" * 70)
    print("\nRESULT:", s.leafSimilar(tree1, tree2), "(expected True)")

    input("\n\n>>> press Enter to run CASE 2 <<<")

    print("\n" + "#" * 70)
    print("CASE 2 — early mismatch: 2,4,5 vs 2,7,5")
    print("watch that the third leaves (5 and 5) are never yielded")
    print("#" * 70)
    print("\nRESULT:", s.leafSimilar(tree5, tree6), "(expected False)")
