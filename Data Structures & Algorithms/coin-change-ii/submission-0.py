class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # either we can take a coin, or we don't.
        # if we take a coin, then we can take any other coin.
        # at any given index, and amount, we can know how many combinations can make amount using only coins[:index]

        coins.sort()

        memo = {}

        def dfs(i, remaining):
            if i >= len(coins):
                return 0
            if remaining == 0:
                return 1
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res = 0
            if remaining >= coins[i]:
                res += dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            
            memo[(i, remaining)] = res
            return res

        return dfs(0, amount)