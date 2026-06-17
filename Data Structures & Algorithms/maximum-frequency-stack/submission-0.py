class FreqStack:

    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int)
        self.index = 0
        

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val)) # we want max-heap for max freq, we also store the index for tie-breaker condition
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()