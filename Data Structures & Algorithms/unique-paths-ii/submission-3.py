class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # dfs(r, c) returns number of ways from r, c to the end

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]

# Time: O(m*n)
# Space: O(m*n) for recursion stack