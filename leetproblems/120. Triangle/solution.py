from math import inf

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = {0: triangle[0][0] }

        for i in range(1, n):
            curr_row = {}
            for j in range(len(triangle[i])):
                a, b = j, j-1
                parent_1 = dp[a] if a in dp else inf
                parent_2 = dp[b] if b in dp else inf
                curr_row[j] = triangle[i][j] + min(parent_1, parent_2)
            dp = curr_row

        res = inf
        for x in dp:
            res = min(dp[x], res)
        return res
        