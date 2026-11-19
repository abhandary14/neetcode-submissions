class Solution:
    def romanToInt(self, s: str) -> int:
        # it is given that the roman numeral is valid every time. so we can say that for for example 99, it will be XCIX and not IXIX (latter is invalid).

        mp = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        res = 0
        for i in range(len(s)):
            # if the current character is less than the next one, then we subtract that from the result, else we add it.
            # IV = -1 + 5, VI = 5 + 1
            if i + 1 < len(s) and mp[s[i]] < mp[s[i + 1]]:
                res -= mp[s[i]]
            else:
                res += mp[s[i]]
        
        return res