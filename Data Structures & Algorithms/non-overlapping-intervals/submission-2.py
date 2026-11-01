class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we don't need a recursive approach here at all
        # we can directly count the number of intervals to remove -> the ones that overlap with others

        # sort based on end time
        res = 0
        intervals.sort(key = lambda x : x[1])

        # check if each interval overlaps with the previous end
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                res += 1
            else:
                prev_end = intervals[i][1]
    
        return res