# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)

        potions.sort()

        result = []

        for spell in spells:
            index = self.binSearchMinimum(potions, success/spell)
            if index <= m:
                result.append(m-index)
            else:
                result.append(0)

        return result



    def binSearchMinimum(self, arr: List[int], target: float) -> int:
        l = 0
        r = len(arr)-1

        while l <= r:
            m = l + (r-l)//2
            if arr[m] >= target:
                # meets condition, try and find a smaller one that meets condition
                r = m - 1

            else:
                l = m + 1

        return r + 1