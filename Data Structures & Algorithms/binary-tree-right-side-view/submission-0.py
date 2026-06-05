# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        lst = []

        q.append(root)

        while q:
            ans = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    ans.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if ans:
                lst.append(ans)
       
        right = []
        for l in lst:
            right.append(l[-1])
        
        return right