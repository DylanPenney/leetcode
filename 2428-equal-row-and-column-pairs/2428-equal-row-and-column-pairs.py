# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = defaultdict(int)
        res = 0

        for row in grid:
            rows[str(row)] += 1

        # column loop
        for i in range(len(grid[0])):
            col = []

            # row loop
            for j in range(len(grid)):
                col.append(grid[j][i])
            res += rows[str(col)]

        return res

        