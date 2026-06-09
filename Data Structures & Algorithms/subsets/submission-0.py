class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:]) # need to append a copy of curr.
                return
            
            # don't include
            backtrack(i+1, curr)
            
            # include
            curr.append(nums[i])
            backtrack(i+1, curr)

            # backtrack
            curr.pop()

        backtrack(0, [])
        return res