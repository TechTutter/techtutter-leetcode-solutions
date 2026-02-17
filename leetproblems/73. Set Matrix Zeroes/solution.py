class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Iterate over all values to find zero cols and rows
        Iterate once more and set 0 if either row or col had zeros
        For 0 extra space you can use first row and first col to store zeros
        """
        rows = len(matrix)
        if rows == 0: return

        cols = len(matrix[0])
        if cols == 0: return

        zero_columns = set()
        zero_rows = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_columns.add(j)
                    zero_rows.add(i)

        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0