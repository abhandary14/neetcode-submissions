class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in mp:
                return [mp[target - nums[i]], i]
            mp[nums[i]] = i