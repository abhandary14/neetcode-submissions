class Solution:
    def hammingWeight(self, n: int) -> int:
        # if we perform any bitwise operation, it automatically does it with its binary representation

        res = 0
        while n > 0:
            res += (n & 1) # this will AND with the last bit. if it is 1, the ans will be 1
            n >>= 1 # right shift by 1
        
        return res