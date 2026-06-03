# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # idx = length - n

        # if idx == 0:
        #     return head.next

        # curr = head
        # for i in range(idx-1):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        # return head

        dummy = ListNode(None)
        dummy.next = head
        l, r = dummy, head

        for _ in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
