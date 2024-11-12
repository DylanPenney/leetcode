# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0 # pointer for current position in s
        r = 0 # pointer for current position in t

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1

        return l == len(s)