class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        for num in candies:

            if num + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)

        return res