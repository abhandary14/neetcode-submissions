class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # either you take the coin, or you don't. you can take a coin multiple times

        # bottom-up DP
        # we take small amount and calculate how many coins for this small amount. then based on that we calculate large amount

        dp = [amount+1] * (amount+1) # we initialize with large values because we want to minimize it
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return -1 if dp[amount] >= amount+1 else dp[amount]

            