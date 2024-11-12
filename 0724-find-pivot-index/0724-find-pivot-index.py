class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(nums)
        leftsum = 0
        for i in range (0, len(nums)):
            leftsum += nums[i]
            if leftsum == rightsum:
                return i
            rightsum -= nums[i]
        return -1
        