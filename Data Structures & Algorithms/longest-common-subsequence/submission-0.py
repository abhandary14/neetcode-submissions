class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dfs(i, j) => tex1[i] == text2[j]? -> include else exclude

        memo = [[None] * len(text2) for _ in range(len(text1))] 

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] is not None:
                return memo[i][j]
            
            # if character is same, then select both and move forward
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dfs(i+1, j+1)
                return memo[i][j]

            # else, try both (move i forward, and move j forward)
            memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[i][j]
        
        return dfs(0, 0)