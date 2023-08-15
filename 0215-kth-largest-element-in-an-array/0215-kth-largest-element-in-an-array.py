import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        heap = []

        for i in nums:
            heapq.heappush(heap,i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)