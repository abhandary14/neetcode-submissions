class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] -> number of ways we can segment remaining number i
        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2, n+1):
            dp[num] = 0 if num == n else num

            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
            

        return dp[n]


