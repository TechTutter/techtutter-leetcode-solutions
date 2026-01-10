class Solution:
    """
    for each cell (r, c) in board:
        if cell is empty: continue
        check if value is unique in its row
        check if value is unique in its column
        check if value is unique in its 3x3 sub-box
    return True
    """
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range (0, 9):
            for j in range (0, 9):
                subsquare_i = i // 3
                subsquare_j = j // 3

                # skip any checks as "." is always valid
                if board[i][j] == ".":
                    continue

                # If board[i][j] is duplicated in its' subsquare, return False
                for a in range(subsquare_i * 3, (subsquare_i + 1) * 3):
                    for b in range(subsquare_j * 3, (subsquare_j + 1) * 3):
                        if board[a][b] == board[i][j] and (a != i or b != j): 
                            return False

                # If boards[i][j] is duplicated in the same row, return False
                for x in range(0, 9):
                    if board[i][x] == board[i][j] and x != j:
                        return False

                # If boards[i][j] is duplicated in the same column, return False
                for x in range(0, 9):
                    if board[x][j] == board[i][j] and x != i:
                        return False

        return True
