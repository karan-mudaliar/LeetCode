class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res = []
        visited = set()

        def backtrack(row, col, idx):
            if idx == len(word):
                return True

            if (row > len(board) - 1 or col > len(board[0]) - 1 or (row,col) in visited
            or row < 0 or col < 0 or word[idx] != board[row][col]):
                return False

            visited.add((row, col)) 
            result = (
                backtrack(row + 1,col,idx + 1) or
                backtrack(row - 1,col,idx + 1) or
                backtrack(row,col + 1,idx + 1) or
                backtrack(row,col - 1,idx + 1)
            )
            visited.remove((row,col))

            return result
        
        for row in range(len(board)):
            for col in range(len(board[0])):
               if backtrack(row,col,0):
                   return True
        
        return False
            

        