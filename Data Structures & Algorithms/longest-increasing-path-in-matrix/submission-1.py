class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Kahn's algorithm bruh
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        indegree = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m) and (0 <= nc < n) and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1
        
        q = deque()

        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    q.append((r, c))

        
        LIS = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m) and (0 <= nc < n) and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))
        
            LIS += 1
        
        return LIS