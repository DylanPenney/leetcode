# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        curr = ""
        for char in s:
            if char != " ":
                curr += char
            elif curr:
                stack.append(curr)
                curr = ""

        if curr:
            stack.append(curr)

        res = str(stack.pop())

        while stack:
            res += " "
            res += stack.pop()

        return res