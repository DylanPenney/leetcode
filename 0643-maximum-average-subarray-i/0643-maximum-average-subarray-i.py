# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        max_sum = sum(nums[:k])
        curr_sum = max_sum

        for r in range(k, len(nums)):
            
            # Update 'window' sum
            curr_sum -= nums[r-k]
            curr_sum += nums[r]

            max_sum = max(max_sum, curr_sum)

        return max_sum / k