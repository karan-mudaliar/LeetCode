class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                end -= 1
            else:
                i += 1
        return nums
        