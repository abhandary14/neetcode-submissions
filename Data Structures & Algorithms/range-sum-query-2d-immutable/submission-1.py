class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.nums = []
        for row in matrix:
            prefix = row[:] # copy of row
            
            for i in range(1, len(prefix)):
                prefix[i] += prefix[i-1]
            
            self.nums.append(prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # ans = 0
        # for i in range(row1, row2+1):
        #     ans += sum(self.matrix[i][col1 : col2+1])
        
        # return ans
        # sumRegion needs to be O(1), so maybe we can do something in the init

        # this is O(n)
        ans = 0
        for i in range(row1, row2+1):
            if col1 > 0:
                ans += self.nums[i][col2] - self.nums[i][col1 - 1]
            else:
                ans += self.nums[i][col2]
        
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)