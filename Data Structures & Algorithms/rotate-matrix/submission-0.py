class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # top to bottom swap
        # transpose

        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            for i in range(len(matrix)):
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]
            top += 1
            bottom -= 1
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]