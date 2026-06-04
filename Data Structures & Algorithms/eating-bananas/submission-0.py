import math
class Solution:
    def calculate(self, piles, rate):
        ans = 0
        for pile in piles:
            ans += int(math.ceil(pile / rate))
        return ans


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxsize = max(piles)
        l, r = 1, maxsize
        res = maxsize

        while l <= r:
            mid = l + (r-l) // 2
            total_hrs = self.calculate(piles, mid)
            if total_hrs <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res
            
            