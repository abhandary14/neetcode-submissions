class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])

        heap = [] # min heap, pair of [end, numPassengers]
        currPass = 0

        for numPass, start, end in trips:
            while heap and heap[0][0] <= start:
                # drop people off everyone whose end time is less than the current start time, and subtract from current passengers
                currPass -= heapq.heappop(heap)[1]
            
            currPass += numPass # add the passengers of the current stop to the current passenges
            if currPass > capacity:
                return False

            # push onto the heap
            heapq.heappush(heap, [end, numPass])
        
        return True