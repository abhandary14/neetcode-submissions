class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n, n

        n = len(cost)
        dp = [0] * (n + 1) # storing the minimum cost to reach step i
        
        # dp[0] = 0 as we can start at 0
        # dp[1] = 0 as we can also start at 1
        # so we start iterating from index 2

        # to get to step i, 
        #    we can come from step i-1 after spending dp[i-1] and paying cost[i-1]
        # or we can come from step i-2 after spending dp[i-2] and paying cost[i-2]
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]