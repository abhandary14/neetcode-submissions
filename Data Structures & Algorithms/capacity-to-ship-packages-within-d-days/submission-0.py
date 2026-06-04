class Solution:
    def checkWeight(self, weights, days, cap):
        ans = 1
        curr = 0

        for i in weights:
            if curr + i > cap:
                ans += 1
                curr = 0
            curr += i
        
        return ans <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = l + (r-l) // 2

            if self.checkWeight(weights, days, mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l