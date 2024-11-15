# Time Complexity: O(m * n)
# Space Complexity: (m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m+1)]

        dp[m-1][n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[row][col] += dp[row+1][col] + dp[row][col+1]

        return dp[0][0]