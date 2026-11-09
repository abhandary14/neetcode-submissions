class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert the interval
        # then merge

        if not intervals:
            return [newInterval]

        # we can use binary search to find the correct insert position
        n = len(intervals)
        target = newInterval[0] # target position
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # insert in the position
        intervals.insert(l, newInterval)

        # merge
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res