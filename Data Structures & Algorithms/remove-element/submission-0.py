class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if an element is val, swap it with the first non-val you encounter
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k