class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        # distances[i] = tuple(dist, coors[i])
        for p in points:
            distances.append((p[0]**2 + p[1]**2, [p[0], p[1]]))

        heapq.heapify(distances)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        
        return res

