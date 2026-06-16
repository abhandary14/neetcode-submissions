class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(i, j):
            area = 0

            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0 # we set it 0 so that we don't count it again for another island
            area = 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i - 1, j)
        
            return area
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea      