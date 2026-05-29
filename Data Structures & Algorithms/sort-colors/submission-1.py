class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        j = 0
        for i in range(3):
            freq = count[i] if i in count else 0
            nums[j : j+freq] = [i] * freq
            j += freq            
        