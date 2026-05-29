class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict as it will at least have one output and not be null

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1  # we're counting the letters in each word. We wanna map 'a' to 0 and 'z' to 25

            res[tuple(count)].append(s)

        return res.values()