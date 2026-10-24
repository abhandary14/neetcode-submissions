class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # subsequence is a non-contiguous subset of an array.
        # bruteforce: generate all subsequences and check if it is increasing
        # at any index, we have two choices. to take this number or not 

        # we define a memo:
        # we do len(nums) + 1 because j can range from -1 to n-1. so we offset it by 1
        memo = [[-1] * (len(nums)+1) for _ in range(len(nums))]

        # dfs(i, j) -> i = current index, j = index of the last included element
        def dfs(i, j):
            if i == len(nums):
                return 0 # if no element left, then length of LIS is 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j) # don't include this element, hence j remains j

            # if no element has been selected so far, or the last selected element is less than current, then we can include it
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # we're calculating length, so if we include an index, then we do 1 +

            memo[i][j+1] = LIS
            return LIS
        
        # initialize j to -1 as we haven't taken anything in the beginning.
        return dfs(0, -1)

# n^2
