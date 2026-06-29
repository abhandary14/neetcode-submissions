class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we can start checking from the borders.
        # find the Os that are connected to borders. then from that Os, recursively check in all directions if there are other Os connected and mark them not to be flipped.
        # then find the remaining Os and flip them
        # we can recursively bfs to check


        dont_flip = set() 
        borderOs = deque()

        ROWS, COLS = len(board), len(board[0])

        # find the Os on the borders
        for i in range(ROWS):
            if board[i][0] == "O":
                borderOs.append((i, 0))
                dont_flip.add((i, 0))
            
            if board[i][COLS-1] == "O":
                borderOs.append((i, COLS-1)) 
                dont_flip.add((i, COLS-1))
        
        for j in range(COLS):
            if board[0][j] == "O":
                borderOs.append((0, j))
                dont_flip.add((0, j))
            
            if board[ROWS-1][j] == "O":
                borderOs.append((ROWS-1, j))
                dont_flip.add((ROWS-1, j))
        
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while borderOs:
            r, c = borderOs.popleft()

            for i, j in offsets:
                newr, newc = r+i, c+j
                if 0 <= newr < ROWS and 0 <= newc < COLS and (newr, newc) not in dont_flip and board[newr][newc] == "O":
                    borderOs.append((newr, newc))
                    dont_flip.add((newr, newc))
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in dont_flip:
                    board[i][j] = "X"