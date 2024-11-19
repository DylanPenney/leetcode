# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum_height = max(0, gain[0])

        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            maximum_height = max(maximum_height, gain[i])

        return maximum_height

# 52, -91, 72
#     -39, 33
# 