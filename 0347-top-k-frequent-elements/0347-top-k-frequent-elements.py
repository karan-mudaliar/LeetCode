import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 0
        ret = sorted(map.keys(), key = lambda x : map[x], reverse = True)

        return ret[:k]
        
        

