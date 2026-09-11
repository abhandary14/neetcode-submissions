class Solution:
    def countSubstrings(self, s: str) -> int:
        # same as before but we count instead of store, also different substrings are considered different palindromes even if the content is same.
        # so we don't need to store them in a set or anything
        
        count = 0
        
        if len(s) == 1:
            return 1

        for i in range(len(s)):
            # even length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # odd length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count
            