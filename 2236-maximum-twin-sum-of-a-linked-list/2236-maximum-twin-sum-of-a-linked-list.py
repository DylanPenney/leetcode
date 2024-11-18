# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # reverse first half of list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is pointing to half way point, reverse list from slow onwards
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        highest_sum = 0

        # first list head, second list head
        l, r = head, prev
        while r:
            highest_sum = max(highest_sum, l.val + r.val)
            l = l.next
            r = r.next

        return highest_sum

        