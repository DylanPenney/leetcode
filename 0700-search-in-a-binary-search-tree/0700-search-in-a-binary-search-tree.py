# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root

        while curr:
            if curr.val == val:
                return curr

            if curr.val > val:
                curr = curr.left
            
            else:
                curr = curr.right

        return None