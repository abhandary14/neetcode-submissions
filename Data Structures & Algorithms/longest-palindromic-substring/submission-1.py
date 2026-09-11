class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) space
        
        idx, longest = 0, 0
        n = len(s)

        # we build a 2D Dp array that stores whether s[i:j] is a palindrome

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # if the two ending are same, and the string between them is a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if longest < j - i + 1:
                        longest = j - i + 1
                        idx = i
        
        return s[idx : idx + longest]

