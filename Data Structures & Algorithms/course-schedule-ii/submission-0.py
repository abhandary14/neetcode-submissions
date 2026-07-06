class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return topo sort of the graph
        # in example 1, it has 2 connected components
        # 1->0 and 2. so it can either be 2, 0, 1 or 0, 1, 2

        adj = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])

        
        indegree = [0] * numCourses
        for i in range(numCourses):
            for c in adj[i]:
                indegree[c] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        idx = 0
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            idx += 1

            for i in adj[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            
        if idx != numCourses:
            return []
        return res
        

