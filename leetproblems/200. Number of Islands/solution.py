from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n, m = len(grid), len(grid[0])
        islands = 0

        def bfs(r: int, c: int) -> None:
            queue: deque[tuple[int, int]] = deque([(r, c)])
            grid[r][c] = "0"
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands