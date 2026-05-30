class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pref, suff = 1, 1

        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        
        return res