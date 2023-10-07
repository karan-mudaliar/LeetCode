class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0
        start, end = 0, len(height) - 1

        while start < end:
            left = height[start]
            right = height[end]
            h = min(left,right)
            area = max(area, h*(end - start))
            if left > right:
                end -= 1
            else:
                start += 1
        return area