# In each turn, we have multiple choices. 
# - take 1st pile, take first two piles, ... take first X piles
# - if both players play optimally, then both will try and increase their score to the max by trying out all possibilities.
# - that means we'd have to store both of their scores, and that'd make things very complicated.
# - So instead, what we can do is only track alice's score. When it is alice's turn, we try to maximize her score
# - When it is bob's turn, we try to minimize alice's score.

# O(n^3) -> damn
# O(n^2)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # dp[alice][i][M] -> i can range from 0 to n, and M can also have the same range
        # alice is a boolean so 2 values
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                prefix = 0

                dp[1][i][M] = 0 # max alice score initilaization when alice's turn
                dp[0][i][M] = float('inf') # min alice score initialization when bob's turn

                for X in range(1, 2*M + 1):
                    if i + X > n:
                        break
                    
                    prefix += piles[i + X - 1]

                    dp[1][i][M] = max(dp[1][i][M], prefix + dp[0][i+X][max(M, X)])
                    dp[0][i][M] = min(dp[0][i][M], dp[1][i+X][max(M, X)])
            
        return dp[1][0][1]