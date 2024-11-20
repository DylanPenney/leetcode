from math import gcd

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            # there are no possible substrings
            return ""

        # return the substring of str1[0:gcd(len(str1), len(str2))]
        return str1[0:gcd(len(str1), len(str2))]