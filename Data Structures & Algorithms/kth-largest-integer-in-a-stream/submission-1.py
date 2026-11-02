# k'th largest is n-k'th smallest. so if we maintain a heap of size k, k'th largest would be 0th smallest
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k

        # make sure heap is of size k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        
