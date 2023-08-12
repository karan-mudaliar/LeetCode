class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_start, col_start = 0 , 0
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while row_start <= row_end and col_start <= col_end:

            for col in range(col_start,col_end+1):
                res.append(matrix[row_start][col])
            
            for row in range(row_start + 1, row_end + 1):
                res.append(matrix[row][col_end])

            for col in reversed(range(col_start,col_end)):
                if row_start == row_end:
                    break
                res.append(matrix[row_end][col])
            
            for row in reversed(range(row_start + 1,row_end)):
                if col_start == col_end:
                    break
                res.append(matrix[row][col_start])
            
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        return res