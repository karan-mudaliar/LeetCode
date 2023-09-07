class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        num_rows, num_cols = len(grid), len(grid[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def bfs(row, col):
            if (row < 0 or col < 0 or row >= num_rows or col >= num_cols 
            or visited[row][col]) or grid[row][col] == '0':
                return

            visited[row][col] = True

            bfs(row + 1, col)
            bfs(row - 1, col)
            bfs(row, col + 1)
            bfs(row, col - 1)

        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1' and not visited[row][col]:
                    count += 1
                    bfs(row,col)

        return count

        