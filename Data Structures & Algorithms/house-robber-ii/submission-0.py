class Solution:
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]


    def rob(self, nums: List[int]) -> int:
        # we need to split the problem into two constraints
        # 1. rob houses from 0 to n-2 (exclude the last house)
        # 2. rob houses from 1 to n-1 (exclude the first house)

        # the recursive function is the same. 
        # - skip the current house OR
        # - rob the current house and skip the next one

        # Here, we can reuse the solution from house robber 1.
        # first we will run it from 0 to n-1,
        # then we will run it from 1 to n.
    
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        