class Solution:
    def search(self, nums: List[int], target: int) -> int:
        piv = self.pivot(nums)
        
        if target == nums[piv]:
            return piv
        left = self.bin(nums[:piv],target)
        right = self.bin(nums[piv:],target)

        print(piv,nums[:piv],nums[piv:])

        if left == -1 and right == -1:
            return -1
        if left == -1:
            return right + piv
        return left

    
    def pivot(self,nums):
        ele = nums[-1]

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > ele:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    def bin(self, arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1