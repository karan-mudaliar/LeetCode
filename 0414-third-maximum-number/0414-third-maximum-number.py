import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nlarg = heapq.nlargest(3, set(nums))
        return nlarg[-1] if len(nlarg) == 3 else nlarg[0]