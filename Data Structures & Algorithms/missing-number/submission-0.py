class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we are given numbers from 0 to n with a single missing number
        # if we assume that the nums were sorted and none of them were missing, then at index 0, there would be 0, and at index n, there would be n.
        # so the net difference of index - num should be 0. 
        # if there is a number missing, then the resulting difference will reflect it

        res = len(nums)
        
        for i in range(len(nums)):
            res += i - nums[i]
        
        return res