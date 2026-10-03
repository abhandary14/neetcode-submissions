class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # either you take the coin, or you don't. you can take a coin multiple times

        memo = {}
        def dfs(a):
            if a == 0: # nothing remaining, 
                return 0
            if a in memo:
                return memo[a]
            
            res = float('inf')
            for c in coins:
                if a - c >= 0:
                    res = min(res, 1 + dfs(a - c))
            
            memo[a] = res
            return res
        
        res = dfs(amount)
        return -1 if res == float('inf') else res