# Time Complextiy: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev

            # move to next element
            prev = curr
            curr = temp

        return prev