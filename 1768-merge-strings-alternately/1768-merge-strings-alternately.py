# Time Complexity: O(m+n)
# Space Complexity: O(1)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0

        merged_string = ""

        while l<len(word1) and r<len(word2):
            merged_string += str(word1[l]) + str(word2[r])
            l += 1
            r += 1

        if l<len(word1):
            merged_string += word1[l:]
        else:
            merged_string += word2[r:]

        return merged_string