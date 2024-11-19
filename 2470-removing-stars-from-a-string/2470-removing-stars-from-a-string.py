# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)