# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = ['a', 'e', 'i', 'o', 'u']

        for char in s:
            if char.lower() in vowels:
                stack.append(char)

        res = ""

        print(stack)

        for i in range(len(s)):
            if s[i].lower() in vowels:
                res += stack.pop()

            else:
                res += s[i] 
        return res