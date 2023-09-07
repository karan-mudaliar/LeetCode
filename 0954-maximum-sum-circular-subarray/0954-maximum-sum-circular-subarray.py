class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax = 0
        maxo = nums[0]
        mini = nums[0]
        currmin = 0
        for num in nums:
            currmax = max(currmax + num, num)
            currmin = min(currmin + num, num)

            maxo = max(maxo, currmax)
            mini = min(mini, currmin)

        return max(maxo, sum(nums) - mini) if maxo > 0 else maxo
            