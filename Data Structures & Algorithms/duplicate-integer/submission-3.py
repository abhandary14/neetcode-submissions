class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            hash_set.add(i)
        
        if len(hash_set) == len(nums):
            return False
        else:
            return True