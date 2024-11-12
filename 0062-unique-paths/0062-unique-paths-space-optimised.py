# Time Complexity: O(m * n)
# Space Complexity: (n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m-1):
            new_row = [1] * n
            for col in range(n - 2, -1, -1):
                new_row[col] = new_row[col+1] + row[col]
            row = new_row

        return row[0]