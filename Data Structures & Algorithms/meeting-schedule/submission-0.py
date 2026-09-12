"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints = []
        for interval in intervals:
            ints.append((interval.start, interval.end))
        
        ints.sort()

        for i in range(len(ints)-1):
            if ints[i][1] > ints[i+1][0]:
                return False
        
        return True