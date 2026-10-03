# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currsum):
            if not node:
                return False
            
            currsum += node.val
            if not node.left and not node.right:
                return currsum == targetSum
            
            return dfs(node.left, currsum) or dfs(node.right, currsum)
        
        return dfs(root, 0)