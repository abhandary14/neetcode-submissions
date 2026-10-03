class Solution:
    def rob(self, nums: List[int]) -> int:
        # if we take the first house, we can't take the last house
        # if we take the last house, we can't take the first house
        # so we return max of the house robber problem for both cases

        if len(nums) == 1:
            return nums[0]

        # house robber
        def helper(nums):
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


        return max(helper(nums[1:]), helper(nums[:-1]))