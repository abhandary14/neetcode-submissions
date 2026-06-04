# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        curr1 = l1
        curr2 = l2
        ans = ListNode(None, None)
        res = ans
    
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                ans.next = ListNode(curr1.val, None)
                curr1 = curr1.next
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


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l, r = 0, len(lists) - 1
        

        def helper(l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = l + (r-l) // 2
            left = helper(l, mid)
            right = helper(mid+1, r)
            return self.merge(left, right)

        return helper(0, len(lists)-1)