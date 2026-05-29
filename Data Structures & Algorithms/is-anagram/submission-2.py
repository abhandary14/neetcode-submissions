class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)

        # if t == s:
        #     return True
        # return False

        if (len(s) != len(t)):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1

        return count_s == count_t