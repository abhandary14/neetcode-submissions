class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # naive solution would be just dfs from each node and count connected components. O(V+E)
        # or we can do a union find -> connect a forest of trees.
        # begin with n connected components and keep merging based on edges

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            
            while res != parent[res]:
                parent[res] = parent[parent[res]] # optimization
                res = parent[res]
            
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
        
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

         
