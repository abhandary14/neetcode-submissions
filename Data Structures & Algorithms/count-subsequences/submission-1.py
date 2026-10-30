class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    # two pointer.
    # recursively: either skip a character in s, or take it only if it matches a character in t

        if len(t) > len(s):
            return 0

        memo = {}
        # memo[(i, j)] = number of substrings that can be formed using s[:i] and t[:j]

        # i = curr index in s, j = curr index in t
        def dfs(i, j):
            if j == len(t): # we found a valid one
                return 1
            
            # j hasn't reached the end of t, but we reached the end of s. so no valid subsequence can be formed
            if i == len(s): 
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            # skip a character in s
            res = dfs(i + 1, j)

            # if they match, then consider the character and move both ahead
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)

# O(2^m) -> m = len(s)
# O(m)