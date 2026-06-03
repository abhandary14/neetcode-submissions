class ListNode:
    def __init__(self, val: int = None):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        q = [ListNode() for _ in range(k)]
        
        for i in range(len(q)-1):
            q[i].next = q[i+1]
        
        q[-1].next = q[0]
        
        self.head = q[0]
        self.tail = q[0]
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        if self.size > 0:
            self.tail = self.tail.next
        
        self.tail.val = value
        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.head.val = None
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
        return True

    def Front(self) -> int:
        return -1 if self.size == 0 else self.head.val

    def Rear(self) -> int:
        return -1 if self.size == 0 else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()