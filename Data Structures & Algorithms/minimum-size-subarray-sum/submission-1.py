class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        l = 0
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r-l+1)
                curr_sum -= nums[l]
                l += 1
            
        return ans if ans != float('inf') else 0

