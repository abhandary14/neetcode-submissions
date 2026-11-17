# n! in the worst case -> n^2 memoized
# space O(n) for the recursion stack

class Solution:
    def jump(self, nums: List[int]) -> int:
        # recursion

        memo = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            if i in memo:
                return memo[i]
            
            end = min(len(nums) - 1, i + nums[i]) # can't go out of bounds
            res = float('inf') # set to maximum

            for j in range(i + 1, end + 1): # jumps can be made from i+1 to the end
                res = min(res, 1 + dfs(j))
                memo[i] = res
            
            return memo[i]
        
        return dfs(0)

