class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = True if matrix[0][0] == 1 else False
        r = len(matrix)#no rows
        c = len(matrix[0])#no columns
    
        row = [1]*r
        col = [1]*c
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
                    
        for i in range(r):
            if row[i]==0:
                for j in range(c):
                    matrix[i][j]=0
                    
        for j in range(c):
            if col[j]==0:
                for i in range(r):
                    matrix[i][j]=0
                    
                
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        