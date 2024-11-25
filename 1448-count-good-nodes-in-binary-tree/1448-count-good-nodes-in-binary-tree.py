# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def backtrack(node: TreeNode, highest_seen: int):
            nonlocal res

            if not node: 
                return None
            
            if node.val >= highest_seen:
                res += 1
                highest_seen = node.val

            backtrack(node.left, highest_seen)
            backtrack(node.right, highest_seen)



        backtrack(root, root.val)

        return res
        
