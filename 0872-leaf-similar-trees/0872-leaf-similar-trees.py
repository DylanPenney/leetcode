# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_value_1 = []
        leaf_value_2 = []

        def dfs(node, arr):
            if not node:
                return

            if not (node.left or node.right):
                arr.append(node.val)
                return

            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(root1, leaf_value_1)
        dfs(root2, leaf_value_2)

        return leaf_value_1 == leaf_value_2
