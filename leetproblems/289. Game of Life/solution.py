class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        count live neighbours
        encode with 0 dead, 1 live, 2 live -> dead, 3 dead -> live
        replace all 2 and 3 with 1 and 0 respectively
        """
        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                # count live neighbours
                live = 0
                for a in range(max(0, i - 1), min(n, i+2)):
                    for b in range(max(0, j - 1), min(m, j+2)):
                        if a != i or b != j:
                            live += 1 if board[a][b] == 1 or board[a][b] == 2 else 0

                # based on live neighbours, act
                if board[i][j] == 0:
                    board[i][j] = 3 if live == 3 else 0
                else:
                    board[i][j] = 2 if live < 2 or live > 3 else 1
                
        for i in range(n):
            for j in range(m):
                board[i][j] = 1 if board[i][j] == 1 or board[i][j] == 3 else 0