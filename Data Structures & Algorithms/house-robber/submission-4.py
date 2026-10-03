class Solution:
    def rob(self, nums: List[int]) -> int:
        # best up to house i-2, best up to house i-1
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        