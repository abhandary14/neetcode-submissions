class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # we will choose the projects that take the minimum capaital and that give the maximum profit

        n = len(profits)
        indices = list(range(n)) # project indices

        # we sort the projects according to the capital it takes.
        indices.sort(key = lambda i : capital[i])

        max_profit = [] # heap
        i = 0

        for _ in range(k): # we can only do k projects
            while i < n and capital[indices[i]] <= w: # initial capital
                heapq.heappush(max_profit, -profits[indices[i]])
                i += 1
            
            if not max_profit:
                break
            
            w -= heapq.heappop(max_profit) # max heap will return negative value, so to increment w, we do -=
        
        return w