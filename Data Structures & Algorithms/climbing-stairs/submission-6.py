class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # dp = [0] * (n + 1)
        first, second = 1, 1

        # dp[1], dp[2] = 1, 2

        # space optimization
        for i in range(n-1):
            temp = first
            first = first + second
            second = temp
        
        return first