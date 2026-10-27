class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # our target is to make subsets as close to sum(stones) / 2 as possible
        # that way, when we smash all stones into each other, we will get the minimum possible remaining stone

        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2) # ceil for odd numbers

        memo = [[None] * (target) for _ in range(len(stones))]

        # dfs(i, total) tracks for stones[:i], what is the total so far
        def dfs(i, total):
            if i == len(stones) or total >= target:
                # absolute diff of the two subsets
                return abs((stoneSum - total) - total)
            if memo[i][total] is not None:
                return memo[i][total]
            
            memo[i][total] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return memo[i][total]
            
        return dfs(0, 0)