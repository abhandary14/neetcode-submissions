class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # for each pick-up location -> while passengers <= capacity
        # cap -= passengers

        events = []
        for trip in trips:
            events.append((trip[1], trip[0]))
            events.append((trip[2], -trip[0]))

        events.sort()
        current_passengers = 0
        for event in events:
            if current_passengers > capacity:
                return False
            current_passengers += event[1]
        
        return True
