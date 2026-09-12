class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra

        n = len(grid)

        q = [(grid[0][0], 0, 0)]
        seen = set()
        
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        while q:
            t, r, c = heapq.heappop(q)

            if (r, c) in seen:
                continue
            
            seen.add((r, c))
            
            if r == n-1 and c == n-1:
                return t
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen):
                    max_t = max(t, grid[nr][nc])
                    heapq.heappush(q, (max_t, nr, nc))
        
        return -1