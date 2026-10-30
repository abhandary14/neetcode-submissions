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
        nums = [1] + nums + [1]

        memo = {}
        def dfs(l, r):
            # no balloons left. can't do anything
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]
        
            memo[(l, r)] = 0 # initialize the max coins to a small value
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1] # since i is the last bln to burst
                coins += dfs(l, i - 1) + dfs(i + 1, r)

                memo[(l, r)] = max(memo[(l, r)], coins)
            
            return memo[(l, r)]
        
        # since we added 1s at both ends, we need to skip them
        return dfs(1, len(nums)-2)

