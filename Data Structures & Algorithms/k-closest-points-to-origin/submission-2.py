class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # dist from origin = x^2 + y^2

        # we could keep a max-heap of size k as well
        # a max heap has the largest element at the top
        # so every element below it will be smaller, and the last element will be the smallest
        max_heap = []
        for x, y in points:
            d = (x*x + y*y) * -1
            if len(max_heap) < k:
                heapq.heappush(max_heap, (d, [x, y]))
            else:
                heapq.heappush(max_heap, (d, [x, y]))
                heapq.heappop(max_heap)
                # can also write:
                # heapq.heappushpop(max_heap, (d, [x, y]))
            
        return [x[1] for x in max_heap]
        