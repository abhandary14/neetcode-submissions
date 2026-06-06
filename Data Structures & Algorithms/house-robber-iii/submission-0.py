# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # two primary cases. we include the root, or we don't include the root

        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # if we select the root, then we can't select the ones immediately below it. so we'll return the max so.
            withRoot = root.val + leftPair[1] + rightPair[1]
            # if we don't select the root, we have the freedom of choosing from where the max is coming
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        
        return max(dfs(root))