class Solution:
    def numDecodings(self, s: str) -> int:
        # at each index, we can take one digit if it is not 0
        # or we can take two digits if it forms a number between 10 and 26

        # how many ways can I decode the substring starting at i?

        memo = {len(s) : 1} # we're going backwards (right to left)

        def dfs(i):
            # if i == len(s):
            #     return 1

            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0

            res = dfs(i+1)
            
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    res += dfs(i+2)
            
            memo[i] = res
            return memo[i]
        
        return dfs(0)



