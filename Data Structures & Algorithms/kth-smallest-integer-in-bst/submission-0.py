# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal till k steps
        
        i = k
        res = None
        def inorder(node):
            nonlocal i, res
            if not node or res is not None:
                return
            
            inorder(node.left)
            i -= 1
            if i == 0:
                res = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return res
            