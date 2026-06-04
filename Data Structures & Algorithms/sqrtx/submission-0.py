class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = l + (r-l) // 2
            if x == mid*mid:
                return mid
            elif x < mid*mid:
                r = mid - 1
            else:
                l = mid + 1
        
        return r