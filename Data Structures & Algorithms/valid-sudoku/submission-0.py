class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for c in row:
                if c == ".":
                    continue
                if c in s:
                    return False
                s.add(c)

        for j in range(0, 9):
            s = set()
            for i in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True