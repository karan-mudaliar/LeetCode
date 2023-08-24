class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        end = start
        ret = []
        if len(nums) == 0:
            return []
        def helper(indexes,nums):
            idx_start , idx_end = indexes

            if idx_start == idx_end:
                return str(nums[idx_start])
            else:
                return "{}->{}".format(nums[idx_start],nums[idx_end])

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = i
            else:
                ret.append((start,end))
                start = i
                end = start
        ret.append((start,end))
        print([helper(x,nums) for x in ret])
        return [helper(x,nums) for x in ret]

