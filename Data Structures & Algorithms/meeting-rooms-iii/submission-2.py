# O(mlogm + mlogn)
# space: O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)] # min heap for available rooms, rooms are index from 0 to n as given in the problem statement. at the start, all rooms are available
        used = [] # min heap of [(end_time, room_number)] -> we will use this to assign a room with the earliest ending time
        
        count = [0] * n # count of meetings for each room

        for start, end in meetings:
            # end time of the top meeting in the heap is less than current start
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used) # pop the room from the used heap
                heapq.heappush(available, room) # put it onto the available heap

            # if no room is available
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start) # calculate when the room will be available
                heapq.heappush(available, room)

            # if any room is available
            room = heapq.heappop(available) # pop the earliest available room
            heapq.heappush(used, (end, room)) # push to the used rooms
            count[room] += 1


        # index of the room with highest meetings
        return count.index(max(count))
        