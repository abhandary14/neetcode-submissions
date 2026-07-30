class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # this is a graph problem
        # we want to link every numerator with every denominator
        # a <-> b <-> c (a is a numerator of b in one example, and b is a numerator of c)
        # ab <-> ac
        # we will assign weights to the edges. so a->b will have weight 4.0, and b->a will have weight 1/4. that'll make it easier for calculation

        adj = defaultdict(list) # Map a -> list of [b, a/b], a/b is given in values
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        # query: a/b
        # src = a, target = b. we need to find the weight of the path from a to b
        def bfs(src, target): # easier to detect a cycle
            if src not in adj or target not in adj:
                return -1
            
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w

                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, weight * w])
                        visit.add(nei)

            return -1



        return [bfs(q[0], q[1]) for q in queries]

