class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <=2:
            return max(nums)
        
        DP = nums[:]

        DP[1] = max(DP[0],DP[1])

        for i in range(2,len(nums)):
            DP[i] = max(DP[i-1],DP[i-2]+nums[i])

        return max(DP[-1],DP[-2])