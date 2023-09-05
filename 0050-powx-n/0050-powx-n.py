class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = abs(n)

        if exp == 0:
            return 1
        if exp % 2 == 0:
            x = self.myPow(x*x, exp//2)
        else:
            x = x * self.myPow(x*x,(exp-1)//2)
        
        return x if n >=0 else 1/x
