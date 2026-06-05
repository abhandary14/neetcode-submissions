"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(grid, r, c, size):

            def check_values(grid, r, c, size):
                sumn = 0
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        sumn += grid[i][j]
                
                if sumn == size*size or sumn == 0:
                    return True
                else:
                    return False

            if check_values(grid, r, c, size):
                return Node(grid[r][c], True, None, None, None, None)
        
            half = size // 2
            topLeft = helper(grid, r, c, half)
            topRight = helper(grid, r, c + half, half)
            bottomLeft = helper(grid, r + half, c, half)
            bottomRight = helper(grid, r + half, c + half, half)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return helper(grid, 0, 0, len(grid))
