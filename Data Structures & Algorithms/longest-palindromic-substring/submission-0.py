class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        idx = 0

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > longest:
                    idx = l
                    longest = r - l + 1
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > longest:
                    idx = l
                    longest = r-l+1
                l -= 1
                r += 1

        return s[idx : idx + longest]               
