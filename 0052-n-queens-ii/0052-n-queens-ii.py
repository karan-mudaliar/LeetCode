class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        cols = set()
        neg = set()
        pos = set()
        count = 0
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            nonlocal count
            if row == n:
                # copy = [''.join(temp) for temp in board]
                # res.append(copy)
                count += 1
            
            for col in range(n):
                if col in cols or (row + col) in pos or (row - col) in neg:
                    continue
                
                cols.add(col)
                neg.add( row - col)
                pos.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                neg.remove(row - col)
                pos.remove(row + col)
                board[row][col] = '.'

        backtrack(0)

        return count


        