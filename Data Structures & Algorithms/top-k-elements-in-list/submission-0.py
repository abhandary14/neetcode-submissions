class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort but
        # we will store the frequencies as keys, and a list of numbers with that frequency as values.
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0) # 1 + the current count. if it does not exist yet, 1 + 0.

        for num, c in count.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
