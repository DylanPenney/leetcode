# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next

        dummy = even

        while even and even.next:
            # move odd to next odd index
            odd.next = even.next
            odd = odd.next

            # move even to next even index
            even.next = odd.next
            even = even.next

        # join even and odd lists together
        odd.next = dummy
        return head


        
        