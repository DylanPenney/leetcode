# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            m = l + (r-l)//2
            row = m // COLS
            col = m % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1

        return False