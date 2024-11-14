# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)

        while l < r:
            m = l + (r-l)//2

            missing_nums = arr[m] - m - 1

            if k <= missing_nums:
                r = m
            else:
                l = m + 1

        return r + k