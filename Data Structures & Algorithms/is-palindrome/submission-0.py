class Solution:
    def checkAlphaNum(self, c):
        return (
            (ord("Z") >= ord(c) >= ord("A")) or 
            (ord("z") >= ord(c) >= ord("a")) or 
            (ord("9") >= ord(c) >= ord("0"))
        )

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.checkAlphaNum(s[left]):
                left += 1
            while left < right and not self.checkAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
        