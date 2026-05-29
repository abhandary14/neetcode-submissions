class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = 0
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] > 1:
                return True
        return False
        