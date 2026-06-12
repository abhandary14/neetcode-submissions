class Solution:
    def totalNQueens(self, n: int) -> int:
        # board = [[0] * n for _ in range(n)] # we don't need this board anymore

        col = set()
        posDiag = set()
        negDiag = set()

        res = 0

        def dfs(r):
            nonlocal res
            # base case
            if r == n:
                res += 1
                return

            # condition check
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                # add queen
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # board[r][c] = 1

                dfs(r+1)

                # remove queen
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                # board[r][c] = 0

        dfs(0)
        return res