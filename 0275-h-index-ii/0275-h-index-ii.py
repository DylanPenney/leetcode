# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        l = 0
        r = n - 1

        while l <= r:
            m = l + (r-l)//2

            if n-m >citations[m]:
                l = m + 1
            else:
                r = m - 1

        return n - l
