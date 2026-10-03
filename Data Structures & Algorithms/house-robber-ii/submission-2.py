class Solution:
    def rob(self, nums: List[int]) -> int:
        # if we take the first house, we can't take the last house
        # if we take the last house, we can't take the first house
        # so we return max of the house robber problem for both cases

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            memo = [-1] * len(nums)
            def dfs(i):
                if i >= len(nums):
                    return 0
                if memo[i] != -1:
                    return memo[i]
                
                memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
                return memo[i]
            
            return dfs(0)


        return max(helper(nums[1:]), helper(nums[:-1]))