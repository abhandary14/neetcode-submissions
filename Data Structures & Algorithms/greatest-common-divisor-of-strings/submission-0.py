class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        g = math.gcd(len(str1), len(str2)) # GCD of the lengths of the two

        return str1[:g]
        
