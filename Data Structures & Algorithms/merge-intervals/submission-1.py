class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals:
            s, e = interval

            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append(interval)
        
        return res