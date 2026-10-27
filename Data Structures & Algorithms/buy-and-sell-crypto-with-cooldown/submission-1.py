class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][j] stores the max profit at day i given j is true (buying) or false (selling)
        dp = [[0] * 2 for _ in range(n+1)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    # if there is a stock to buy, then we buy and subtract from our profit, else we go in deficit
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    # we cannot buy unless we sell so we keep the buying state to false
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        
        return dp[0][1]

    # O(n * 2) = O(n)
    # O(n * 2) = O(n)