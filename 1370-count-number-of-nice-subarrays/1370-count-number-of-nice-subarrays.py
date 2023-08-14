class Solution(object):
    def numberOfSubarrays(self, nums, k):
        for i in range(len(nums)):
            nums[i] = nums[i] % 2

        hashmap = {}
        hashmap[0] = 1
        sums = 0
        count = 0

        for i in range(len(nums)):
            sums += nums[i]
            if sums in hashmap:
                hashmap[sums] += 1
            else:
                hashmap[sums] = 1
            if sums - k in hashmap:
                count += hashmap[sums-k]
        return count