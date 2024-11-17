# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0

        max_vowels = 0
        curr_vowels = 0

        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1


        max_vowels = curr_vowels

        for r in range(k, len(s)):
            if curr_vowels == k:
                return k

            # window l to r
            if s[r] in vowels:
                curr_vowels += 1

            # move left pointer
            if s[l] in vowels:
                curr_vowels -= 1

            l += 1

            max_vowels = max(curr_vowels, max_vowels)

        return max_vowels