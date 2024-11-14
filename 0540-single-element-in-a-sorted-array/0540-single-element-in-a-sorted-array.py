# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l != r:
            m = l + (r-l)//2

            if m % 2:
                m -= 1

            # as m is even, if nums[m] == nums[m+1], 
            # then the missing number must be before m
            if nums[m] == nums[m+1]:
                l = m + 2 # plus 2 as m+1 is equal to m

            else:
                r = m

        return nums[l]