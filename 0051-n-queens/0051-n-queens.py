class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        neg = set()
        pos = set()

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
            
            for col in range(n):
                if col in cols or (row + col) in pos or (row - col) in neg:
                    continue
                
                cols.add(col)
                neg.add(row - col)
                pos.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                neg.remove(row - col)
                pos.remove(row + col)
                board[row][col] = '.'
        
        backtrack(0)

        return res
        