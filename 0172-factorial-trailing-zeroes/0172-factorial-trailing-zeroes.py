class Solution:
    def trailingZeroes(self, n: int) -> int:

        base = 5
        zeros = 0

        while base <= n:
            zeros += n // base
            base *= 5

        return zeros
        