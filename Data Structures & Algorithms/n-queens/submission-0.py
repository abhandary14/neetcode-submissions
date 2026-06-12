class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        # we will use hashsets to store where queens have been placed
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        
        # for every row, check if a queen can be placed at a given column
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue # don't place queen there
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."


        dfs(0)
        return res