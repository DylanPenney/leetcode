# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = index - stackI

            stack.append((index, temperature))

        return res