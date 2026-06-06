# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # postorder traversal

        stack = [root]
        visit = set()
        parents = {root : None}

        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                if curr.val == target:
                    p = parents[curr]
                    if not p:
                        return None
                    if p.left == curr:
                        p.left = None
                    if p.right == curr:
                        p.right = None

            elif curr not in visit:
                visit.add(curr)
                stack.append(curr)
                if curr.left:
                    stack.append(curr.left)
                    parents[curr.left] = curr
                if curr.right:
                    stack.append(curr.right)
                    parents[curr.right] = curr
        
        return root
             