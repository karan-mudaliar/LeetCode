class Solution:
    def climbStairs(self, n: int, i = 0,seen= {}) -> int:
        
        if n == 0:
            return 1
        if n < 0:
            return 0
        if (n,i) in seen:
            return seen[(n,i)]
        
        ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        seen[(n,i)] = ways
        
        return ways