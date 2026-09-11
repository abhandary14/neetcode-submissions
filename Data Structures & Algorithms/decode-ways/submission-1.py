class Solution:
    def numDecodings(self, s: str) -> int:
        # number of ways the thing can be decoded

        # at each index i, we have the option -> 
        # 1. take 1 digit (if not 0)
        # 2. take 2 digits (if it forms a number between 10 and 26)

        # we solve for -> how many ways can I decode the substring starting at index i

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1) # we can select 1 digit if the val is not 0.
            
            # if we're not at the last index
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                res += dfs(i+2)
            
            dp[i] = res
            return res
         
        return dfs(0)

    # O(2^n), O(n) for the recursion stack
