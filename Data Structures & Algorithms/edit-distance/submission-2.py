class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # at each index, we need to perform 3 operations.
        # delete the character and check if the next one in w1 matches the one in w2
        # insert a character into w1 to see if it matches and move on
        # replace a character from w1 to see if it matches and move on
        # if it matches, then by default skip


        # d[i][j] returns the minimum number of operations required to convert word1[i:] to word2[j:]

        m = len(word1)
        n = len(word2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i 
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]
