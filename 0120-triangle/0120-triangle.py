class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        arr = [[0 for _ in row] for row in triangle]

        arr[rows-1] = triangle[rows - 1]

        for row in reversed(range(rows-1)):
            for col in range(len(arr[row])):
                arr[row][col] = triangle[row][col] + min(arr[row + 1][col], arr[row+1][col+1])  
        print(arr)
        return arr[0][0]
        