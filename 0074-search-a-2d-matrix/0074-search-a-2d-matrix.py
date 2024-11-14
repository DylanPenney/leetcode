class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l,r = 0, ROWS * COLS - 1
        while l <= r:
            mid = l + (r-l)//2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] < target:
                # too low
                l = mid + 1
            elif matrix[row][col] > target:
                # too hight
                r = mid - 1
            else:
                # found it
                return True
        return False