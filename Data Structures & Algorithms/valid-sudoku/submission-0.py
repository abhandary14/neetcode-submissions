class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_rows = defaultdict(set)
        hash_cols = defaultdict(set)
        hash_square = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in hash_rows[row] or board[row][col] in hash_cols[col] or board[row][col] in hash_square[(row // 3, col // 3)]):
                    return False
                hash_rows[row].add(board[row][col])
                hash_cols[col].add(board[row][col])
                hash_square[(row // 3, col // 3)].add(board[row][col])

        return True
            