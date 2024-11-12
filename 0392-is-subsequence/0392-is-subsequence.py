class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        pointer = 0
        for i in t:
            if i == s[pointer]:
                pointer+=1
            if pointer >= len(s):
                return True
        return False