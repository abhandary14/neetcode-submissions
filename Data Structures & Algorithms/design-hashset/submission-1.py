class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[self._hash(key)]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[self._hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next     

    def contains(self, key: int) -> bool:
        cur = self.set[self._hash(key)]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

    def _hash(self, key: int) -> int:
        return key % len(self.set)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)