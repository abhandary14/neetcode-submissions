class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we need to check for every word in wordDict, if a word matches a the string starting at index i
        # if yes, then recursively check for the substring starting at i + len(w)

        # O(m^n * t), where t is the max length of any word
        # space O(n)

        memo = {len(s) : True} # memo[i] -> whether s[i:] can be segmented or not

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i : i + len(word)]:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)



