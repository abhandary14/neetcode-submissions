class Solution:
    def reorganizeString(self, s: str) -> str:
        #task scheduler

        freq = collections.Counter(s)

        maxHeap = [[-v, c] for c, v in freq.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count < 0:
                prev = [count, char]

        return res

