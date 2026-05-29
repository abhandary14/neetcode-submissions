class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = prices[0]
        
        for i in prices:
            if i < curr: # track the current lowest
                curr = i
            profit = max(profit, i - curr)

        return profit
