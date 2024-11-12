# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)

        for index, num in enumerate(nums):
            if leftsum + num == rightsum:
                return index

            leftsum += num
            rightsum -= num

        return -1