class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for a very large matrix, the recursion depth might hit. so we can use a stack based iterative approach.

        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = "0"

            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        stack.append((nx, ny))
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count