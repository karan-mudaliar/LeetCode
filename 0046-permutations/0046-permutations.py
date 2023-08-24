class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []

        def swap(arr,i,j):
            arr[i],arr[j] = arr[j],arr[i]

        def y(i,nums,ret):
            if i == len(nums) - 1:
                ret.append(nums[:])
            else:
                for j in range(i,len(nums)):
                    swap(nums,i,j)
                    y(i+1,nums,ret)
                    swap(nums,i,j)
        y(0,nums,ret)
        return ret