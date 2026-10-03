class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n 

        def dfs(i):
            # if index is greater than n
            if i >= n:
                # return true if index is n
                return i == n
            if memo[i] != -1:
                return memo[i]
            
            # climb one, or two stairs
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        
        return dfs(0)