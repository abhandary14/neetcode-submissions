class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # max BFS depth

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0 # count the number of fresh fruit to convert them to rotten

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while fresh > 0 and q: # while there are fresh fruits left and there are some nodes in the queue
            for _ in range(len(q)): # keep popping from the queue and process it
                r, c = q.popleft()

                for dr, dc in directions: # from every node, go in each direction and rot bananas. append the rotten banana positions to the queue
                    row, col = r + dr, c + dc

                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1): # if the current position is in bounds and there is a fresh banana, rot it and increment time
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1 # if there are fresh fruits left at the end, return -1. Remember, diagonal bananas can't be rotten. they have to be directly adjacent.
        