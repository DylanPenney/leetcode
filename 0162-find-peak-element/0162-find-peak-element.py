# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if r == 0:
            return 0

        while l < r:
            m = l + (r-l)//2

            if nums[m+1] < nums[m]:
                # there is a peak to the right
                r = m
            else:
                # peak must be to the left
                l = m + 1

        return l