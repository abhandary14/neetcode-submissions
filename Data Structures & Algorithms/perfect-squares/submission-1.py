class Solution:
    def numSquares(self, n: int) -> int:
        # subtract any perfect square from n, then recurse on remaining 

        dp = [n] * (n+1)
        dp[0] = 0

        for rem in range(1, n+1):
            for i in range(rem):
                if i*i > rem:
                    break
                dp[rem] = min(dp[rem], 1 + dp[rem - i*i])
        
        return dp[n]