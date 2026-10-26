class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dfs(i, j) represents minimum to reach i, j
        # O(2^(m+n)) -> normal recursion
        # O(m + n)

        # to avoid rework, we memoize -> O(m*n)

        m = len(grid)
        n = len(grid[0])

        memo = [[None] * n for _ in range(m)]

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            
            # if list index out of range, return infinity to indicate invalid path
            # check this before checking memo as invalid path can occur before
            if i == m or j == n:
                return float('inf')

            if memo[i][j] is not None:
                return memo[i][j]

            memo[i][j] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            return memo[i][j]
        
        return dfs(0, 0)