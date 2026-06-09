class MedianFinder:

    def __init__(self):
        # every element in the small should be smaller than every element in the large.
        # for that, small has to be a maxHeap, since we can compare the largest element from it with the smallest element in the large minHeap.
        # we will insert elements into small by multiplying by -1.
        # both the heaps should be equal size, or differ by max 1 in case the stream is of odd length.
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # if the top of small is larger than top of large, then move it to large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # if length is uneven, i.e., differs by two, then handle it
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2

        