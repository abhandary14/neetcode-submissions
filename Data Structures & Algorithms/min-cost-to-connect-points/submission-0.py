# (n^2 log n) time
# (n^2) space

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        res = node
        
        while self.parent[res] != res:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        
        return res
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parent[py] = px
        self.size[px] += self.size[py]

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm

        n = len(points)
        uf = UnionFind(n)

        edges = []

        for i in range(n): # n^2
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                edges.append((dist, i, j))
        
        edges.sort() # sort edges based on distance (nlogn)

        res = 0

        for dist, u, v in edges: # (n)
            if uf.union(u, v):
                res += dist
        
        return res

        