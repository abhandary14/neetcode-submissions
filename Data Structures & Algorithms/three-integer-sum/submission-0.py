class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                curr = nums[i]+ nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l < r:
                        l += 1
        return ans




