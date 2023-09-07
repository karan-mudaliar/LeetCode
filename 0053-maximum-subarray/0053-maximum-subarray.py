class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxo,currmax = nums[0], 0

        for num in nums:
            currmax = max(currmax + num,num)
            maxo = max(currmax,maxo)

        return maxo
        