class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [[None for _ in range(n)] for _ in range(n)]
        row_start,col_start = 0, 0
        row_end, col_end = n - 1, n - 1
        count = 1
        while row_start <= row_end and col_start <= col_end:

            for col in range(col_start, col_end + 1):
                arr[row_start][col] = count
                count += 1
            
            for row in range(row_start + 1, row_end + 1):
                arr[row][col_end] = count
                count += 1
            
            for col in reversed(range(col_start,col_end)):
                arr[row_end][col] = count
                count += 1
            
            for row in reversed(range(row_start+1,row_end)):
                arr[row][col_start] = count
                count += 1
            
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1
              

        return arr