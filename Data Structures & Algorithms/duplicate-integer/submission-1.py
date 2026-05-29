class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for num in nums:
            numMap[num] = 0

        for num in nums:
            numMap[num] += 1
            if numMap[num] > 1:
                return True

        return False

         