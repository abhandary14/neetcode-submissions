class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # create a frequency map of characters in the string
        maxHeap = [[-cnt, char] for char, cnt in count.items()]

        heapq.heapify(maxHeap)

        prev = None # we will append to the result the character that is the most frequent, but that wasn't just used
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap: # there's nothing in the maxHeap but there's still an element left
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 # decrement the count, but since we've negated the values, use += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res