class Solution:
    def rob(self, nums: List[int]) -> int:
        # skip or don't skip the house

        # option 1 -> skip the house and solve for i+1
        # option2 -> take the house and solve for i+2

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i+1), nums[i] + dfs(i+2))
        
        # return dfs(0)

        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        
        return dfs(0)