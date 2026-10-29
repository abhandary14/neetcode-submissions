class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        memo = {}

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c, prevVal): # O(m * n)
            if min(r, c) < 0 or r >= m or c >= n or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            res = 1
            for dr, dc in dirs:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            memo[(r, c)] = res
            return res
    
        res = 0

        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, float('-inf')))

        return res

# O(m * n)
# O(m*n)
