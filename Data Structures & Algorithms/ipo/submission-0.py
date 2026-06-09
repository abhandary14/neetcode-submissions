class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[c, p] for c, p in list(zip(capital, profits))]
        projects.sort()

        maxHeap = []

        i = 0 # since projects is sorted, we can iterate using a global variable
        for _ in range(k):
            while i < len(projects):
                if projects[i][0] <= w:
                    # we're pushing negative of profit since we need to pop the max profit for every possible project requiring <= w capital
                    heapq.heappush(maxHeap, [-projects[i][1], projects[i][0]])
                    i += 1
                else:
                    break
            
            if maxHeap:
                prof, cap = heapq.heappop(maxHeap)
                w -= prof # subtracting because prof is a negative value.
        
        return w