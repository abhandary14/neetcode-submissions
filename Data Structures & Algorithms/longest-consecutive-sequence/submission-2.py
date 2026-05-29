class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        setNums = set(nums)
        for n in setNums:
            if (n-1) not in setNums:
                length = 1
                while(n + length) in setNums:
                    length += 1
                longest = max(length, longest)
        return longest
