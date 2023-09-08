class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        if nums[0] > nums[1]:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                end = mid
            
            else:
                start = mid

        return start