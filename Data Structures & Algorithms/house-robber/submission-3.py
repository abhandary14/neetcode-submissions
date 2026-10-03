class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums))
        def dfs(i):
            # can't rob a house if there is no house
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            # skip the house, or take the current house and skip the next
            memo[i] = max(dfs(i+1), nums[i] + dfs(i + 2))
            return memo[i]
        
        return dfs(0)