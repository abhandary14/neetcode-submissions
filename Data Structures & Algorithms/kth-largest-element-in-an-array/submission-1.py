class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest = n-kth smallest

        heapq.heapify(nums)
        n = len(nums)

        target = n - k
        
        while target > 0:
            heapq.heappop(nums)
            target -= 1
        
        return heapq.heappop(nums)