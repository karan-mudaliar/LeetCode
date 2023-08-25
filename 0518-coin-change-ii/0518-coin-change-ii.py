class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        seen = {}
        return self.helper(amount,coins,seen)
    
    def helper(self, amount, coins, seen, i = 0):

        if amount == 0:
            return 1
        if amount < 0:
            return 0
        
        if (amount,i) in seen:
            return seen[(amount,i)]
        ways = 0
        for j in range(i,len(coins)):
            ways += self.helper(amount - coins[j],coins,seen,j)
        seen[(amount,i)] = ways

        return ways