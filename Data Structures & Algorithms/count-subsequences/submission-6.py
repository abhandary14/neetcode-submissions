class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    # two pointer.
    # recursively: either skip a character in s, or take it only if it matches a character in t

        # O(m*n), O(n) -> we can optimize the space
        
        m = len(s)
        n = len(t)

        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        dp[n], nextDp[n] = 1, 1
        

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # skip the current i
                nextDp[j] = dp[j]

                # common pitfall -> compare s[i] with *t[j]* and not s[j]
                if s[i] == t[j]:
                    nextDp[j] += dp[j + 1]
                
            dp = nextDp[:]
        
        return dp[0]


        # memo = {}
        # # memo[(i, j)] = number of substrings that can be formed using s[:i] and t[:j]

        # # i = curr index in s, j = curr index in t
        # def dfs(i, j):
        #     if j == len(t): # we found a valid one
        #         return 1
            
        #     # j hasn't reached the end of t, but we reached the end of s. so no valid subsequence can be formed
        #     if i == len(s): 
        #         return 0
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # skip a character in s
        #     res = dfs(i + 1, j)

        #     # if they match, then consider the character and move both ahead
        #     if s[i] == t[j]:
        #         res += dfs(i + 1, j + 1)
            
        #     memo[(i, j)] = res
        #     return res
        
        # return dfs(0, 0)

# O(m * n) -> m = len(s), n = len(t)
# O(m * n)