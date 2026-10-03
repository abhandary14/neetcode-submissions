class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 2^n, n

        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            # cost of current step + min cost of next two steps
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        # we can start at either 0 or 1
        return min(dfs(0), dfs(1))