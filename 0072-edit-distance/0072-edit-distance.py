class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = [[i for i in range(len(word1)+1)] for _ in range(len(word2)+1)]

        for row in range(1,len(DP)):
            DP[row][0] = DP[row - 1][0] + 1
        
        for row in range(1,len(DP)):
            for col in range(1,len(DP[row])):
                if word2[row - 1] == word1[col - 1]:
                    DP[row][col] = DP[row -1][col - 1]
                else:
                    DP[row][col] = min(
                        DP[row-1][col - 1],
                        DP[row][col - 1],
                        DP[row - 1][col]
                    ) + 1
        return DP[-1][-1]      