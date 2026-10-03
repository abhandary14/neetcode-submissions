class Solution:
    def numDecodings(self, s: str) -> int:
        # at each index, we can take one digit if it is not 0
        # or we can take two digits if it forms a number between 10 and 26

        # how many ways can I decode the substring starting at i?

        dp = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0": # 0 ways to decode a substring starting at 0
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i < len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i+1] < "7"):
                dp[i] += dp[i+2]

                #dp[i] = dp[i+1] + dp[i+2] effectively, but dp[i+2] is conditional
        
        return dp[0]



