class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is a single connected component without cycles.
        # we know the graph is connected if the number of given nodes n matches the number of visited nodes
        # we know the graph doesn't have a cycle if we don't visit the same node twice. We will need to keep track of the 'previous' node.

        # tree must have n-1 edges
        if len(edges) != n-1:
            return False

        # get adjacency list
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
    
        # DFS
        visit = set()
        
        def dfs(node, prev):
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor in visit:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        if not dfs(0, -1): # start with a dummy node as prev
            return False
        
        return len(visit) == n

