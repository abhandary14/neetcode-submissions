# in the bruteforce, we tried "what if we burst this balloon first"
# to optimize this, we'll have to think "what if we burst this balloon last"
# if balloon i is the last to burst between the indices l and r, then at that moment, 
# - everything inside (l...r) except i is already gone
# - the neighbors of i are fixed: nums[l-1] on the left and rums[r+1] on the right
# - so ans = nums[l-1] * nums[i] * nums[r+1]
# - the remaining work can be divided into two equal independent parts:
# - from (l ... i-1) and (i+1 ... r) -> this gives us overlapping sub-problems to cache


# this is O(n^3) time and O(n^2) space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums) # we calculate n before adding 1s as they're not real elements in nums
        nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)] # n + 2 because of the coins calculation logic, and since we added the 1s at the ends

        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        
        return dp[1][n]

