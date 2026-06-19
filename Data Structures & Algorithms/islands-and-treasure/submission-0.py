class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-source BFS.
        # if we BFS from each node, we need to mark visited nodes so we don't visit them again. This will lead to many nodes being left out.
        # we need to start BFS from the treasure chests simultaneously and populate each cell with the nearest distance.
    
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addPosition(r, c):
            if (r<0 or r==ROWS or c<0 or c==COLS or (r, c) in visit or grid[r][c]==-1):
                return

            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        # add to the queue layer by layer
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addPosition(r + 1, c)
                addPosition(r, c + 1)
                addPosition(r - 1, c)
                addPosition(r, c - 1)
            
            dist += 1