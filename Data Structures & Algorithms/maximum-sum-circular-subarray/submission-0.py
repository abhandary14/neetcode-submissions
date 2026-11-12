class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # let's consider a subarray in the middle of the array
        # this subarray can be either the one with the max sum, 
        # OR there could be a subarray that wraps around that is the max sum (last few + first few elements)
        # if the wrapped around elements are the max sum, then this subarray in between must be the minimum sum
        # so we do kadane's algorithm, but we keep track of the global maximum, AND the global minimum

        # remember the ans can be negative, hence we initialize it with nums[0]
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = 0, 0 # curr max and curr min are running minimum and maximum sum

        total = 0 # total sum of the array, we can either calculate beforehand, or while we iterate

        for num in nums:
            total += num

            currMax = max(currMax + num, num)
            globalMax = max(globalMax, currMax)

            currMin = min(currMin + num, num)
            globalMin = min(globalMin, currMin)

        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax