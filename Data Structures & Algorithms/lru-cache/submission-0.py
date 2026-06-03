class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        # dummy nodes. Left -> least recent, Right -> most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        # whenever we get a item, we need to update it to the most recently used item
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove and evict the least recently used
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert at right
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev