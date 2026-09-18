class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        memo = {}

        def dfs(x):
            if x == 0:
                return 1
            if x < nums[0]:
                return 0
            if x in memo:
                return memo[x]

            res = 0
            for num in nums: 
                if x - num < 0:
                    break
                res += dfs(x - num)
            
            memo[x] = res
            return res
        
        return dfs(target)