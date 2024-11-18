# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        while r < len(chars):
            
            char = chars[r]
            occurances = 0

            while r < len(chars) and chars[r] == char:
                r += 1
                occurances += 1

            chars[l] = char
            l += 1

            if occurances > 1:
                for c in str(occurances):
                    # add to list as characters
                    chars[l] = c
                    l += 1

        return l
