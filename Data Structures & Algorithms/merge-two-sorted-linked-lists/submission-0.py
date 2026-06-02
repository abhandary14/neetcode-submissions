# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        ans = ListNode(None, None)
        res = ans

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                ans.next = ListNode(curr1.val, None)
                curr1 = curr1.next
                ans = ans.next
            else:
                ans.next = ListNode(curr2.val, None)
                curr2 = curr2.next
                ans = ans.next
            
        
        while curr1:
            ans.next = ListNode(curr1.val, None)
            ans = ans.next
            curr1 = curr1.next
        while curr2:
            ans.next = ListNode(curr2.val, None)
            ans = ans.next
            curr2 = curr2.next

        return res.next