class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # we need to store the last position of each letter

        last = {} # size can be at most 26 as there are only 26 lowercase characters
        for i, c in enumerate(s):
            last[c] = i # will store last i for every c
        
        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c]) # if that character appears later, then the substring has to end there

            if i == end: # at any point if we reach end, we append to the result
                res.append(size)
                size = 0

        return res