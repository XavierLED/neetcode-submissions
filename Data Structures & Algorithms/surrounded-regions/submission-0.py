class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def capture(r, c):
            if(r < 0 or c < 0 or r >= rows or c >= cols
            or board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            for dr, dc in directions:
                row, col = r + dr, c + dc
                capture(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1) or (c == 0 or c == cols - 1) :
                    capture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"