class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target:
            return True

        for i in range(3):
            for row in range(len(mat)):
                for col in range(row+1,len(mat[0])):
                    mat[row][col],mat[col][row] = mat[col][row], mat[row][col]

            for i in range(len(mat)):
                mat[i] = mat[i][::-1]

            if mat == target:
                return True           

        return False
                