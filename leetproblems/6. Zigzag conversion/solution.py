class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        curr = 0
        direction = 1  # 1 = down, -1 = up

        for c in s:
            rows[curr] += c

            if curr == 0:
                direction = 1
            elif curr == numRows - 1:
                direction = -1

            curr += direction

        return ''.join(rows)