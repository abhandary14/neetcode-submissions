class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        index = 0
        res = 0

        def backtrack(index, curr):
            nonlocal res
            if index == len(nums):
                xor = 0
                for r in curr:
                    xor ^= r
                res += xor
                return
            
            backtrack(index+1, curr) # don't include
            
            curr.append(nums[index]) # include. instead of including, we can simply xor
            backtrack(index+1, curr)
            
            curr.pop() # remove
            
        backtrack(0, [])
        return res