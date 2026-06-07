# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            # we need to store null nodes as well
            if not curr:
                res.append("#")
            else:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(nodes[0])

        queue = deque([root])

        i = 1
        while queue:
            curr = queue.popleft()
            curr.left = TreeNode(nodes[i]) if nodes[i] != "#" else None
            curr.right = TreeNode(nodes[i+1]) if nodes[i+1] != "#" else None
            i += 2

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return root
