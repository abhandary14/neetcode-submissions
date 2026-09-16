class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_prod, min_prod = 1, 1

        for n in nums:
            if n == 0:
                max_prod, min_prod = 1, 1
                continue
            
            temp = n * max_prod # we want to preserve this as we're updating max_prod. To calculate min_prod, we want the original value of max_prod.

            max_prod = max(n * max_prod, n * min_prod, n)
            min_prod = min(temp, n * min_prod, n)
        
            res = max(res, max_prod)
    
        return res