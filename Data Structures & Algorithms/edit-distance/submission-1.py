class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # at each index, we need to perform 3 operations.
        # delete the character and check if the next one in w1 matches the one in w2
        # insert a character into w1 to see if it matches and move on
        # replace a character from w1 to see if it matches and move on
        # if it matches, then by default skip


        # dfs(i, j) returns the minimum number of operations required to convert word1[i:] to word2[j:]

        m = len(word1)
        n = len(word2)

        memo = {}

        def dfs(i, j):
            # if we reached end of word1, then we need to insert all the remaining characters from word2
            if i == m:
                return n - j

            # if we reached the end of word2, then all remaining characters from word1 must be deleted
            if j == n:
                return m - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # if it already matches, then
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            # delete from w1, vs insert into w1
            # so if we delete, it is equivalent to moving the index forward by 1
            # if we insert, then we'd obv insert the matching character, so it is equivalend to moving the w2 pointer forward
            res = min(dfs(i + 1, j), dfs(i, j + 1))

            # replace a character -> we'd replace the character then we'd move both pointers forward
            res = min(res, dfs(i + 1, j + 1))
            
            memo[(i, j)] = res + 1
            return res + 1 # we add 1 for the current operation
        
        return dfs(0, 0)
