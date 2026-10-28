class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # O(m * n)
        # O(m * n) for recursion stack

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        # memo[(i, j)] says if s3[k:] can be formed using s1[i:] and s2[j:]

        # i -> pointer to s1, j -> pointer to s2, k -> pointer to s3
        def dfs(i, j, k):

            # return true if both i and j have reached the end of their strings.
            if k == len(s3):
                return (i == len(s1) and j == len(s2))
            
            if (i, j) in memo:
                return memo[(i, j)]
            

            # if either s1[i] or s2[j] matches s3[k], then increment that pointer.
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    res = True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    res = True
            
            # mismatch
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0, 0)
