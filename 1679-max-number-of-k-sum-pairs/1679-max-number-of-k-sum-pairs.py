# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1

        res = 0

        nums.sort()

        while l < r:
            lr_sum = nums[l] + nums[r]
            if lr_sum == k:
                res += 1
                l += 1
                r -= 1
            elif lr_sum > k:
                r -= 1
            else:
                l += 1
        return res
