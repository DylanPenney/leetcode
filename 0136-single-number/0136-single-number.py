# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # weird xor hack
            res ^= num

        return res