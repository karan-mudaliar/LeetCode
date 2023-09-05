class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        H = {}

        for idx, val in enumerate(nums):
            if val not in H:
                H[val] = idx 
            else:
                if abs(H[val] - idx) <= k:
                    return True
                H[val] = idx



        return False
        