from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # count, assign
        # we also need to make sure that the size of the array is divisible by groupsize

        # we will put the keys of the hashmap into a heap and then use the elements in sequential order. if any frequency becomes 0, we pop that element

        if len(hand) % groupSize:
            return False

        freq = Counter(hand)

        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1

                if freq[i] == 0:
                    if i != minHeap[0]: # if the frequency is zero, but it is not tbe minimum element, we can't form a straight hand.
                        return False
                    heapq.heappop(minHeap)

        return True