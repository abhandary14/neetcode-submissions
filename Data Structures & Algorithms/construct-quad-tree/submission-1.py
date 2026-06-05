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
        def helper(r, c, size):

            # sumn = 0
            # for i in range(r, r + size):
            #     for j in range(c, c + size):
            #         sumn += grid[i][j]
            
            sumn = prefix[r+size][c+size] - prefix[r][c+size] - prefix[r+size][c] + prefix[r][c]

            if sumn == size*size or sumn == 0:
                return Node(grid[r][c], True, None, None, None, None)
        
            half = size // 2
            topLeft = helper(r, c, half)
            topRight = helper(r, c + half, half)
            bottomLeft = helper(r + half, c, half)
            bottomRight = helper(r + half, c + half, half)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        # time optimization. we can build a prefix array to store sums and then we can look values up in constant time to check if all values are same
        n = len(grid)
        prefix = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, len(grid)+1):
            for j in range(1, len(grid)+1):
                prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]


        return helper(0, 0, len(grid))
