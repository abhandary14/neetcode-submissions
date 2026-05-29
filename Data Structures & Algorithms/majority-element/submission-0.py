class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        elem = None

        for i in nums:
            if count == 0:
                elem = i
            if elem == i:
                count += 1
            else:
                count -= 1
        
        return elem