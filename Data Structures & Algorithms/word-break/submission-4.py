class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we need to check for every word in wordDict, if a word matches a the string starting at index i
        # if yes, then recursively check for the substring starting at i + len(w)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
            
        return dp[0]