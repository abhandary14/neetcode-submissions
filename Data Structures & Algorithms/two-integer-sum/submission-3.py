class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in hashmap and hashmap[d]!=i:
                return [hashmap[d], i]
            hashmap[nums[i]] = i

            