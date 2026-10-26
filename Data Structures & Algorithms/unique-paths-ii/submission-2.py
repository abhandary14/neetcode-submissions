class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dfs(r, c) returns number of ways from r, c to the end

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [[None] * n for _ in range(m)]

        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if memo[r][c] is not None:
                return memo[r][c]
            
            memo[r][c] = dfs(r+1, c) + dfs(r, c+1)
            return memo[r][c]
        
        return dfs(0, 0)

# Time: O(2^(m+n))
# Space: O(m+n) for recursion stack