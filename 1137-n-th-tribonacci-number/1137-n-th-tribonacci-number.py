# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n+1) # from 0 to n
        
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]