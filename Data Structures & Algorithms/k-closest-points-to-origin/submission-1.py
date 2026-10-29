class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, j in points:
            dist = i**2 + j**2
            heap.append([dist, i, j])
        
        heapq.heapify(heap)

        res = []
        while k > 0:
            dist, i, j = heapq.heappop(heap)
            res.append([i, j])
            k -= 1
        return res