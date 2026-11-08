# but we can use two heaps.
# heap Left -> max_heap that stores the smaller half of the elements
# heap Right -> min_heap that stores the larger half of the elements

# always have the left heap have the same number of elements as the right heap (difference in size at most 1)
# ensure all numbers in the `left` heap are less than the numbers in the `right` heap

class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None: # O(m log n)
        if self.right and num > self.right[0]: # if num is greater than the top of the right heap, push it to the right. the right heap holds the larger values
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1 * num) # left is a max heap
        
        if len(self.left) > len(self.right) + 1:
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * val)


    def findMedian(self) -> float: # O(m) for m queries
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        
        elif len(self.left) < len(self.right):
            return self.right[0]
        
        return (-1 * self.left[0] + self.right[0]) / 2.0
        