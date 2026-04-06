from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n, m = len(board), len(board[0])

        def bfs(r: int, c: int) -> None:
            queue: deque[tuple[int, int]] = deque([(r, c)])
            board[r][c] = "S"  # safe
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        queue.append((nr, nc))

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r in (0, n-1) or c in (0, m-1)):
                    bfs(r, c)

        for r in range(n):
            for c in range(m):
                board[r][c] = "O" if board[r][c] == "S" else "X"
