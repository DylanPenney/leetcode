# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        # one count for each lower case english letter
        count1 = [0] * 26
        count2 = [0] * 26

        if n1 != n2:
            return False

        for i in range(0, n1):
            count1[ ord(word1[i]) - ord('a') ] += 1
            count2[ ord(word2[i]) - ord('a') ] += 1

        for i in range(0, 26):
            if bool(count1[i]) != bool(count2[i]):
                return False

        count1.sort()
        count2.sort()

        for i in range(0, 26):
            if count1[i] != count2[i]:
                return False

        return True

        