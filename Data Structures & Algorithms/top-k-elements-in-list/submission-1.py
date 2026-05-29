class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort but
        # we will store the frequencies as keys, and a list of numbers with that frequency as values.
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] # +1 because the freq of any number can be 0 to n
        res = []

        for num in nums:
            count[num] = 0
        for num in nums:
            count[num] += 1

        for i in count:
            freq[count[i]].append(i)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res