class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod, minprod = 1, 1

        res = nums[0]

        for n in nums:
            if n == 0:
                maxprod, minprod = 1, 1
            
            temp = n * maxprod
            maxprod = max(n * maxprod, n * minprod, n)
            minprod = min(temp, n * minprod, n)

            res = max(res, maxprod)
        
        return res