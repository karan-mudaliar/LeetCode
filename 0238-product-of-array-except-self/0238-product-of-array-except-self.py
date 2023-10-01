class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in nums]
        right = left[:]

        Lprod,Rprod = 1, 1
        for i in range(len(nums)):
            left[i] = Lprod
            Lprod *= nums[i]
        
        for i in reversed(range(len(nums))):
            right[i] = Rprod
            Rprod *= nums[i]

        for i in range(len(nums)):
            left[i] = left[i] * right[i]
       
        return left

        