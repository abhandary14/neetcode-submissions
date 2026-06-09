class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, subset):
            nonlocal res

            xor = 0
            for num in subset:
                xor ^= num
            res += xor

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res