class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # BRUH

        # there's two cases -> 
        # - if the next character is not '*', then the current character must match (directly or via a '.'), and we move both pointers forward
        # - if the next character is '*', then we have two choices
        # - - skip the entire part 'x*'
        # - - use the pattern to match the character from the string and stay on the same index to potentially match more

        # this is O(m*n) time and O(m*n) space

        m = len(s)
        n = len(p)

        # can s[i:] be matched by p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True # s[m:] == s[n:] == "" (null string)

        for i in range(m, -1, -1): # i can be m !
            for j in range(n - 1, -1, -1):
                match = (i < m) and (s[i] == p[j] or p[j] == ".")

                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2]
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]
        
        return dp[0][0]

        # def dfs(i, j):
        #     if j == n:
        #         return i == m # if we've reached the end of the pattern, then we return true only when we've reached the end of the string

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # the string matches so far as long as i < m, and the characters match directly or via a "."
        #     match = (i < m) and (s[i] == p[j] or p[j] == ".") # case 1

        #     if (j + 1) < n and p[j + 1] == "*":
        #         memo[(i, j)] = (dfs(i, j + 2) or    # don't use "*"
        #                 (match and dfs(i + 1, j)))  # use "*"
        #         return memo[(i, j)]

        #     if match:
        #         memo[(i, j)] = dfs(i + 1, j + 1)
        #         return memo[(i, j)]
            
        #     memo[(i, j)] = False
        #     return False
        
        # return dfs(0, 0)