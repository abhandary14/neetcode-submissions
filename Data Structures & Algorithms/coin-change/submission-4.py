class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # either you take the coin, or you don't. you can take a coin multiple times

        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            
            mincoins = float('inf')
            # for every denomination
            for coin in coins:
                # if amount left after selecting coin
                if remaining - coin >= 0:
                    # update mincoins
                    mincoins = min(mincoins, 1 + dfs(remaining - coin))
            
            memo[remaining] = mincoins
            return memo[remaining]
        
        res = dfs(amount)
        return res if res != float('inf') else -1