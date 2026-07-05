class Solution:
    def getAdj(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
        
        return adj

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection using kahn's algorithm
        adj = self.getAdj(numCourses, prerequisites)

        # calculate indegree
        indegree = [0] * numCourses
        for i in range(numCourses):
            for to in adj[i]:
                indegree[to] += 1
        
        # BFS
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        idx = 0
        # res = [0] * numCourses

        while q:
            curr = q.popleft()
            # res[idx] = curr
            idx += 1

            for to in adj[curr]:
                indegree[to] -= 1
                if indegree[to] == 0:
                    q.append(to)
            
        if idx != numCourses:
            return False
        return True



