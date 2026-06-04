# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, end):
        prev = None
        curr = head
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        dummy = ListNode(0, head)
        prev_group_tail = dummy
        group_head = head

        while length >= k:
            end = group_head
            for _ in range(k):
                end = end.next

            group_tail = group_head
            new_group_head = self.reverse(group_head, end)

            prev_group_tail.next = new_group_head
            group_tail.next = end

            prev_group_tail = group_tail
            group_head = end

            length -= k

        return dummy.next