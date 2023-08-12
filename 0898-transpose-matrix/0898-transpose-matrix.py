class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        new = [[None for _ in matrix] for _ in matrix[0]]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                new[col][row] = matrix[row][col]

        return new