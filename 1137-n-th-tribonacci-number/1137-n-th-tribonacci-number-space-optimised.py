# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0, 1, 1]

        for i in range(3, n+1):
            next_dp = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = next_dp

        return dp[-1]