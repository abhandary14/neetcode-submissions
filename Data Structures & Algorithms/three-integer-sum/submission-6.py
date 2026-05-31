class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                sumn = nums[i] + nums[l] + nums[r]
                if sumn == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif sumn < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans 

