class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we take or don't take an element, and we can take any number of times.

        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i]) # we don't increment the index if we're selecting the element. we keep selecting the same element till we can. 
            curr.pop()
        
            dfs(i+1, curr, total)
        
        res = []
        dfs(0, [], 0)
        return res