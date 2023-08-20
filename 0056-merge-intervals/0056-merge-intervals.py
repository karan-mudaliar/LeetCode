class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ret = []
        start , end = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if end >= curr_start:
                end = max(end,curr_end)
            else:
                ret.append([start,end])
                start = curr_start
                end = curr_end
        ret.append([start,end])

        return ret