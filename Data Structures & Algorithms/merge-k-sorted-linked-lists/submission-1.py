# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0) # dummy
        curr = res
        min_heap = []

        # we add heads of each node onto the heap
        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, NodeWrapper(lst))
        
        # now, we pop -> returns the minimum since all lists are sorted
        # if the list has a next element, then we push that onto the heap
        # then we keep doing this until the heap is empty
        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(node_wrapper.node.next))

        return res.next