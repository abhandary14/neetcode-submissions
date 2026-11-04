# we sort by enqueue time so we can process each task in order
# then at each index i, we can add all tasks with enqueue time less than or equal to the current time onto the heap.
# if the heap is empty, we can jump to the next task's enqueue time
# otherwise, we pop the task with the shortest processing time, update time, and record the current index.


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # preserve the original ordering by appending index
        for i, t in enumerate(tasks):
            t.append(i)
        
        # sort based on enque time
        tasks.sort(key=lambda t: t[0]) 

        res, minHeap = [], []

        # index of the current task
        i, time = 0, tasks[0][0] # we will start at the enqueue time of the first task

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                # we only care about processing time and the index
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap: # CPU idle: we're waiting for time to pass
                time = tasks[i][0] # skip to the enqueue time of the first task
            else: # CPU is not idle    
                processTime, idx = heapq.heappop(minHeap)
                time += processTime
                res.append(idx)
        
        return res