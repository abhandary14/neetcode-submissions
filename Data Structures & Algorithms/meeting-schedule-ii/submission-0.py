"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # convert to list of intervals
        ints = []
        for interval in intervals:
            ints.append((interval.start, interval.end))

        # sort the intervals
        ints.sort()

        # we will use min heap to store the end times of meetings
        min_heap = []

        # for each interval, if the earliest end time is less than the incoming meeting,
        # then it means we can reuse the room, so pop the heap and append the new one
        # if the times coincide, then we simply append it to the min heap 
        for interval in ints:
            if min_heap and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        
        # so min-heap will then store the required number of rooms.
        return len(min_heap)

