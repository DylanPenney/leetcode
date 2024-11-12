# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next

        slow, fast = head, head
        prev = ListNode(next=head)

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the mid point of the linked list
        prev.next = slow.next

        return head

        