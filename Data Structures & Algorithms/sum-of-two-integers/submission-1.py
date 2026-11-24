class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # binary representation of 0
        max_int = 0x7FFFFFFF # binary representation of 2^32 - 1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        

        return a if a <= max_int else ~(a ^ mask)