# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)

        for num in arr:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        occurances = defaultdict(int)
        for number, frequency in counter.items():
            if frequency not in occurances:
                occurances[frequency] = 0
            occurances[frequency] += 1

        for frequency in occurances:
            if occurances[frequency] > 1:
                return False

        return True