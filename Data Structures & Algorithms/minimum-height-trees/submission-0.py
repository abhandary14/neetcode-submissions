# Time: O(V * (V+E))
# Space: O(V)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges: # Space O(v)
            adj[u].append(v)
            adj[v].append(u)
        
        # O(V + E)
        # calculate the height of the tree
        def dfs(node, parent): # we need to store the parent so we don't visit it again
            ht = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                ht = max(ht, 1 + dfs(nei, node))
            
            return ht
        
        min_ht = n # what if it looks like a linked list 
        res = []

        for i in range(n): # O(v)
            curr_ht = dfs(i, -1) # parent of root = -1
        
            if curr_ht == min_ht:
                res.append(i)
        
            elif curr_ht < min_ht:
                res = [i]
                min_ht = curr_ht
        
        return res