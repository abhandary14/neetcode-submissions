class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # our target is to make subsets as close to sum(stones) / 2 as possible
        # that way, when we smash all stones into each other, we will get the minimum possible remaining stone

        stoneSum = sum(stones)
        target = stoneSum // 2

        dp = [[0] * (target + 1) for _ in range(len(stones)+1)]
        
        # dp[i][total] represents max sum that is less than total, achievable with stones[:i] 
            
        for i in range(1, len(stones) + 1):
            for total in range(target + 1):
                if total >= stones[i-1]:
                    # if the stone fits, then we take the maximum of taking it vs skipping it
                    dp[i][total] = max(dp[i-1][total], dp[i-1][total - stones[i-1]] + stones[i - 1])
                else:
                    # else just skip it
                    dp[i][total] = dp[i-1][total]

        return (stoneSum - dp[len(stones)][target]) - dp[len(stones)][target]
        # so dp[len(stones)][target] stores the maximum sum less than target achievable when we consider the entire array