class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        stack = []

        for start, end in points:
            if stack and stack[-1][1] >= start:
                curr_start,curr_end = stack.pop()
                stack.append([max(curr_start,start),min(curr_end,end)])
            else:
                stack.append([start,end])
        
        return len(stack)