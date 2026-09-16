class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # last index will be out of bounds if s -> 0 to len(s)-1

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                len_w = len(w)
                if i + len_w <= len(s) and s[i: i + len_w] == w:
                    dp[i] = dp[i + len_w]
                
                if dp[i]:
                    break
            
        return dp[0]


