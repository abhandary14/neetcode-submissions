# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        q.append(root)

        while q:
            right = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    right = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            if right:
                res.append(right)
        
        return res