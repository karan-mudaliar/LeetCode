class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1

        while start ** 2 <= x:
            start += 1

        return start - 1