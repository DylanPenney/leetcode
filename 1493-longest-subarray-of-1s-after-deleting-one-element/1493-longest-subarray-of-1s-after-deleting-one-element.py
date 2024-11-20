# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1

        l = 0
        r = 0

        while r <= len(nums)-1:
            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                k += int(nums[l] == 0)
                l += 1

            r += 1

        return r - l - 1