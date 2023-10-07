class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0 

        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] == k:
                nums.pop(end)
                nums.pop(start)
                end -= 2
                count += 1
            elif nums[start] + nums[end] > k:
                end -= 1
            else:
                start += 1

        return count
