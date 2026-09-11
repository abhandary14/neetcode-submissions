class Solution:
    def numDecodings(self, s: str) -> int:
        # number of ways the thing can be decoded

        # at each index i, we have the option -> 
        # 1. take 1 digit (if not 0)
        # 2. take 2 digits (if it forms a number between 10 and 26)

        # we solve for -> how many ways can I decode the substring starting at index i
        n = len(s)
        dp = {n : 1} # stores the number of ways to decode the substring starting at s

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]

