class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] # +1 because range is non-inclusive

        res = []

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for i in count:
            freq[count[i]].append(i)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res