class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])

        # if it is a square matrix, we transpose in place
        if ROWS == COLS:
            for r in range(ROWS):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
            return matrix
        
        # if it is not square, we create a new matrix
        res = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
            
        return res

# checking if it is a square matrix saves a bit of space when thinking about the ammortized complexity. for a million queries, if half of them are square matrices, we save quite a bit of auxiliary space