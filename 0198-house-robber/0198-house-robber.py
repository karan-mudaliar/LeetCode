class Solution:
    def rob(self, nums: List[int]) -> int:
        DP = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        DP[0] = nums[0]
        DP[1] = max(nums[0],nums[1])
        if len(nums) == 2:
            return DP[1]
        for i in range(2,len(nums)):
            DP[i] = max(DP[i-1],nums[i]+DP[i-2])
        print(nums)
        print(DP)
        return max(DP[-1],DP[-2])
        