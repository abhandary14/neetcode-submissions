class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is a single connected component without cycles.
        # we know the graph is connected if the number of given nodes n matches the number of visited nodes
        # we know the graph doesn't have a cycle if we don't visit the same node twice. We will need to keep track of the 'previous' node.

        # get adjacency list
        adj = [[] for _ in range(n)]
        for i, j in edges:
            if i == j:
                return False
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        stack = [0]

        while stack:
            curr = stack.pop()

            if curr in visit:
                return False
            else:
                visit.add(curr)
                neighbors = adj[curr]
                
                for neighbor in neighbors:
                    if neighbor not in visit:
                        stack.append(neighbor)

        if len(visit) == n:
            return True
        return False