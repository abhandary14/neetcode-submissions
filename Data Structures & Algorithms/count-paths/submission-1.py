class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # since recursion was 2^(m+n), we can memoize and reduce it to m*n

        memo = {} # memo[(i, j)] stores result of dfs(i, j)

        # dfs(i, j) returns number of ways to reach m, n from i, j
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= m or j >= n:
                return 0
            
            # at each index, we have 2 choices, so it will be 2^(m+n)
            # recursion stack O(m+n)
            res = dfs(i + 1, j) + dfs(i, j + 1)

            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)