class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # kinda like dp[1] and dp[2]
        first, second = 1, 2

        # same as if we were using a dp array but optimized
        for i in range(3, n+1):
            curr = first + second
            first = second
            second = curr
        
        return second