class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # we process the most frequent tasks first to avoid idle time

        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # pairs of [-c, idleTime]

        while max_heap or q:
            time += 1
            if max_heap:
                # we do +1 because the heap stores negative values; so to decrement we add 1
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    # append how many times we need to do the task, and then at what time it'll be available again (after n idle time)
                    q.append([cnt, time + n])
            
            # if the first one in the queue is available, then we add the count to the heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time