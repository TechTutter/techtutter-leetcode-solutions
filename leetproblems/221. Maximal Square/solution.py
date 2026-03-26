class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        if i == 0 or j == 0:
            dp[i][j] == matrix[i][j]
        elif matrix[i][j] == 0:
            dp[i][j] == 0
        else:
            pick left_predecessor, top_predecessor, diagonal_predecessor
            best_square[i][j] = matrix[i][j] + min(all predecessors)   
        '''
        m, n = len(matrix), len(matrix[0])
        res = 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    left = dp[i][j-1]
                    top = dp[i-1][j]
                    diag = dp[i-1][j-1]
                    prev_square = min(left, top, diag)
                    dp[i][j] = 1 + prev_square
                res = max(res, dp[i][j])

        return res * res