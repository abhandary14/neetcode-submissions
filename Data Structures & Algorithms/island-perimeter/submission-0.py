class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs. Whenever you reach a boundary or water, add 1. base case 
        # we start the dfs at the first land we get.

        visit = set()

        def dfs(i, j):
            # base case -> out of bounds, or cell is water
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            # base case -> cell already visited, we can't add anything again
            if (i, j) in visit:
                return 0
            
            visit.add((i, j))

            # recurse in all directions
            perim = 0
            perim += dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)

            return perim
        
        # find the first land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)