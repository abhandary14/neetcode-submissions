class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        n = len(nums)
        k = total // 2
        
        # recursively check each index and include it in the subset. if it reaches k, then return true

        dp = [[False] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= k:
            dp[0][nums[0]] = True
        
        for i in range(1, n):
            for curr in range(1, k + 1):
                not_take = dp[i - 1][curr]

                take = False
                if curr - nums[i] >= 0:
                    take = dp[i - 1][curr - nums[i]]
                
                dp[i][curr] = take or not_take

        return dp[n-1][k] 

