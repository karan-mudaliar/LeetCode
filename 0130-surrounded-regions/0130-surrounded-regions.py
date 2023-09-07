class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows, ncols = len(board), len(board[0])
        
        visited = [[False for _ in range(ncols)] for _ in range(nrows)]
        
                    
        def bfs(row, col):
            if row < 0 or row >= nrows or col < 0 or col >= ncols or visited[row][col] or board[row][col] == 'X':
                return
            visited[row][col] = True
            bfs(row - 1, col)
            bfs(row + 1, col)
            bfs(row, col - 1)
            bfs(row, col + 1)

        for row in range(nrows):
            for col in range(ncols):
                if (row == 0 or row == nrows - 1 or col == 0 or col == ncols - 1) and board[row][col] == 'O':
                    bfs(row, col)

        for row in range(nrows):
            for col in range(ncols):
                board[row][col] = 'O' if visited[row][col] else 'X'



        return