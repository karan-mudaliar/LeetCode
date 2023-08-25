# class Solution:
#     def minPathSum(self, grid: List[List[int]],i = 0,j = 0,dist = 0) -> int:
#         seen = {}
#         if i == len(grid) - 1 and j == len(grid[0]) - 1:
#             return grid[i][j]

#         if i > len(grid) - 1 or j > len(grid[0]) - 1:
#             return float('inf')

#         if (i,j) in seen:
#             return seen[(i,j)]

#         seen[(i,j)] = min(self.minPathSum(grid,i + 1,j,dist)
#         , self.minPathSum(grid,i ,j + 1,dist)) + grid[i][j]
#         return seen[(i,j)]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize a 2D DP array to store the minimum path sum
        dp = [[0] * cols for _ in range(rows)]
        
        # Base case: the destination cell
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
        
        # Initialize the last row and last column
        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = dp[i + 1][cols - 1] + grid[i][cols - 1]
        for j in range(cols - 2, -1, -1):
            dp[rows - 1][j] = dp[rows - 1][j + 1] + grid[rows - 1][j]
        
        # Fill in the DP array iteratively
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        
        return dp[0][0]
