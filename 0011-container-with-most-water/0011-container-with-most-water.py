# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l <= r:

            # Area of water between pole at index r and pole at index l
            max_water = max(max_water, (r-l) * min(height[r], height[l]))

            # Then we move the smaller pole towards the other
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_water