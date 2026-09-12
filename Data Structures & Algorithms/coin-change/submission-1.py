class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # either you take the coin, or you don't. you can take a coin multiple times

        # backtracking solution would be taking each coin, then checking if it adds up to the total

        memo = {} # number of coins to make this 'amount'

        def dfs(amount):
            if amount == 0:
                return 0 # for 0 amount, we don't need any coins
            if amount in memo: # if already found,
                return memo[amount]

            res = 1e9

            for coin in coins: # for every coin, solve the problem for (amount - coin)
                if amount - coin >= 0: # can't go down a negative path
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res # store the number of coins for each amount
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
            