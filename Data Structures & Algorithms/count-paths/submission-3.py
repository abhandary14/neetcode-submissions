class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(m*n)
        # O(m*n)

        # we can optimize the space to O(n) if we only maintain one row
        currRow = [1] * n

        for i in range(m-1):
            nextRow = [1] * n
            for j in range(n-2, -1, -1):
                nextRow[j] = nextRow[j + 1] + currRow[j]
            
            currRow = nextRow # move down (update row m-1 times)
        
        return currRow[0]
