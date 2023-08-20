class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uni = 0
        for num in nums:
            uni ^= num
        return uni