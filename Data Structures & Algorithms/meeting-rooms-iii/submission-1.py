class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Approach: simulate the allocation. For each meeting, scan every room.
        # Time: O(m log m + m * n), Space: O(n). With n <= 100 this passes.

        # Sort meetings by start time (start times are unique).
        # This also enforces the rule that delayed meetings run in order of
        # their ORIGINAL start time: an earlier meeting is always processed
        # (and claims a room) before a later one.
        meetings.sort()

        rooms = [0] * n          # rooms[i] = time at which room i becomes free
        meeting_count = [0] * n  # meeting_count[i] = meetings held in room i

        for start, end in meetings:
            min_room = 0   # room that frees up earliest (lowest index on ties)
            found = False  # did we find a room that is already free at `start`?

            # Scan rooms in index order, so the first free room we hit
            # is automatically the lowest-numbered free room.
            for i in range(n):
                # Meetings are half-open [start, end), so a room that frees up
                # exactly at `start` is available.
                if rooms[i] <= start:
                    found = True
                    meeting_count[i] += 1
                    rooms[i] = end
                    break

                # Room i is busy. Track the room that becomes free soonest.
                # Strict `<` keeps the lower index when two rooms free up
                # at the same time.
                if rooms[i] < rooms[min_room]:
                    min_room = i

            if found:
                continue

            # Every room is busy. The meeting waits for the earliest-freeing
            # room and keeps its original duration, so it ends at
            # (time that room frees up) + (end - start).
            meeting_count[min_room] += 1
            rooms[min_room] += (end - start)

        # list.index returns the FIRST occurrence of the max,
        # which is the lowest-numbered room, as the problem requires on ties.
        return meeting_count.index(max(meeting_count))