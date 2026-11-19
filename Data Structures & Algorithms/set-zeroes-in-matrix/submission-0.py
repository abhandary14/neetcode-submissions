class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])

        # if we keep setting zeroes, then eventually we will set all values in the matrix to 0.
        # to make sure we only make the rows and columns 0 where there was 0 originally, we keep track of them in two arrays rows and cols.

        rows, cols = [False] * n, [False] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    rows[i], cols[j] = True, True
        
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0