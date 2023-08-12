class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        nums = sorted(list(nums))
        maxi = 0
        count = 1
        if len(nums) <= 1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                count = 1
            else:
                count += 1
            maxi = max(maxi,count)
        return maxi
        