# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                # pivot is after mid
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1

        return nums[l]