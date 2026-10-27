class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # either we can take a coin, or we don't.
        # if we take a coin, then we can take any other coin.

        coins.sort()

        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # dp[index][amount] -> number of combinations to make amount, given we only have coins[index:]

        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins)-1, -1, -1):
            for remaining in range(amount + 1):
                if remaining >= coins[i]:
                    dp[i][remaining] = dp[i+1][remaining] + dp[i][remaining - coins[i]]

        return dp[0][amount]

