class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node):
            visit.add(node)

            for neighbor in adj[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count