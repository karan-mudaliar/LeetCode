class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ret = matrix[:]
        for row in range(len(matrix)):
            for col in range(row+1,len(matrix[0])):
                matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix