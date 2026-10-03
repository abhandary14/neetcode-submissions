class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n, 1

        # at each step, we need the minimum cost of the next one, or two steps.
        # so we can just keep updating the cost at each step with the minimum cost of the next, or the next two step
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])