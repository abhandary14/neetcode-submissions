class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        # for i in range(len(nums)):
        #     mp[nums[i]] = i
        
        # for i in range(len(nums)):
        #     d = target - nums[i]
        #     if d in mp and mp[d] != i:
        #         return [i, mp[d]]

        for i in range(len(nums)):
            d = target - nums[i]
            if d in mp:
                return [mp[d], i]
            mp[nums[i]] = i