class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        arr = [[0 for _ in matrix[0]] for _ in matrix]
        maxi = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    if matrix[row][col] =='1':
                        arr[row][col] = 1
                else:
                    if matrix[row][col] =='1': 
                        arr[row][col] = 1 + min(
                            arr[row - 1][col - 1],
                            arr[row - 1][col],
                            arr[row][col - 1]
                        )
                maxi = max(maxi,arr[row][col])
        print(arr)
        return maxi ** 2  