# we can:
# 1. dfs for every query. This would be O(n * (V + E)) (n = number of queries) -> n can be 100^2
# 2. we can build a indirect prerequisite map by DFS from each node. then query. -> O(V*(V+E) + n). much less complex than multiplying by 100^2
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(c):
            if c not in prereqMap:
                prereqMap[c] = set()
            
                for prereq in adj[c]:
                    prereqMap[c] |= dfs(prereq) # union of hashsets
            
                prereqMap[c].add(c)
            
            return prereqMap[c]
        
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        prereqMap = {} # map every course -> hashset of indirect prereqs
        for c in range(numCourses):
            dfs(c)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res