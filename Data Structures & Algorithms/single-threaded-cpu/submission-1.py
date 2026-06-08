class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # when we pop, we can add the processing time to the current timestamp

        for i, task in enumerate(tasks):
            task.append(i)

        tasks.sort()
        res = []
        minHeap = []

        time = tasks[0][0]

        index = 0
        while index < len(tasks) or minHeap:
            if not minHeap and time < tasks[index][0]:
                time = tasks[index][0]

            while index < len(tasks) and tasks[index][0] <= time:
                heapq.heappush(minHeap, (tasks[index][1], tasks[index][2]))
                index += 1

            p, i = heapq.heappop(minHeap)
            res.append(i)
            time += p

        return res