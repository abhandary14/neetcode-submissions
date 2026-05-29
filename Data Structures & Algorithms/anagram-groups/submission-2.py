class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # dictionary where the key is the count array, which will be the same for all anagrams.
            res[tuple(count)].append(s) # we use tuple(count) because lists are mutable, and dictionary keys can't be mutable
        return res.values()