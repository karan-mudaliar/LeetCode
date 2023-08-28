class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_idx,l_num = self.mini(nums)
        print(l_idx,l_num,"mini")
        if l_idx is None: 
            nums = nums.reverse()
            return
        g_idx, g_num = self.greater(nums,l_num)
        print(g_idx, g_num,"greater")
        self.swap(l_idx,g_idx,nums)
        print(nums,'swap') 
        return self.rev(l_idx+1,nums)


    
    def mini(self,nums):
        
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i + 1]:
                return i,nums[i]
        return None,None

    def greater(self,nums, num):
        for i in reversed(range(len(nums))):
            if nums[i] > num:
                return i,nums[i]
        return None, None

    def swap(self,less_idx,great_idx,nums):
        nums[less_idx], nums[great_idx] = nums[great_idx], nums[less_idx]

    def rev(self, idx, nums):
        nums[idx:] = nums[idx:][::-1]











