# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def helper(node):
            nonlocal max_dia
            if not node:
                return 0
            
            left_depth = helper(node.left)
            right_depth = helper(node.right)

            max_dia = max(max_dia, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        helper(root)
        return max_dia