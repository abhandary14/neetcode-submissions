class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(2^(m+n)) -> normal recursion
        # O(m + n)

        # to avoid rework, we memoize -> O(m*n)

        m = len(grid)
        n = len(grid[0])

        # dp[i][j] represents minimum cost to reach the end form i, j

        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m-1][n] = 0 # minimum cost to reach the end is zero. (m-1, n) for correct computationi

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]