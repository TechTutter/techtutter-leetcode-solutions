class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        flatten the matrix, and use a regular binary search
        mid % len(matrix) will give the col
        mid // len(matrix) will give the row
        """
        n = len(matrix)
        m = len(matrix[0])
        size = n * m

        lo, hi = 0, size - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // m
            col = mid % m
            curr = matrix[row][col]
            if curr == target: return True
            if curr < target: lo = mid + 1
            else: hi = mid - 1
        return False