class Solution:
    def climbStairs(self, n: int,mem = None) -> int:
        if mem is None:
            mem = {0:1,1:1}
        if n < 0:
            return 0
        if n in mem:
            return mem[n]
        mem[n] = self.climbStairs(n - 1,mem) + self.climbStairs(n - 2,mem)
        return mem[n]
        