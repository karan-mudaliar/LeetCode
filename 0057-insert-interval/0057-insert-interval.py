class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ret = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        start, end = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            curr = intervals[i]
            curr_start, curr_end = curr[0], curr[1]

            if curr_start <= end:
                end = max(end,curr_end)
            else:
                ret.append([start,end])
                start = curr_start
                end = curr_end
        ret.append([start,end])
        return ret