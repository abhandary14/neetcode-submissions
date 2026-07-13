class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # spanning tree
        # in an acyclic graph, for n nodes, there are n-1 edges.
        # since this problem says that there's exactly one edge that makes it cyclic, for n nodes this implies that there are exactly n edges.
        # so:

        n = len(edges)

        # now we can perform union-find to detect the edge that's causing cycles.
        par = [i for i in range(n+1)] # ith node -> parent
        rank = [1] * (n+1)

        def find(node):
            if node != par[node]:
                par[node] = find(par[node]) # path compression

            return par[node]


        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]: # union by rank
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]