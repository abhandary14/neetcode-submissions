# n! in the worst case -> n^2 memoized / bottom-up
# space O(n) for the recursion stack / O(n) bottom-up

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n

        dp[-1] = 0 # can reach the last index from the last index with 0 jumps

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]