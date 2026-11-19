class Solution:
    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n:
            # digit = n % 10
            # digit **= 2
            # res += digit
            
            res += (n % 10) ** 2
            n //= 10
        
        return res

    def isHappy(self, n: int) -> bool:
        # Floyd's cycle detection

        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            # move the fast two times
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)

            # move the slow two times
            slow = self.sumOfSquares(slow)

        return True if fast == 1 else False