class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # boundary conditions, and all conditions that would falsify the recursion
            if (r < 0 or c < 0) or (r >= m or c >= n) or (word[i] != board[r][c]) or (r, c) in path:
                return False
            
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or # move down
                dfs(r, c + 1, i + 1) or # move right
                dfs(r - 1, c, i + 1) or # move up
                dfs(r, c - 1, i + 1)    # move left
            )

            path.remove((r, c))

            return res
        
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
                
        return False