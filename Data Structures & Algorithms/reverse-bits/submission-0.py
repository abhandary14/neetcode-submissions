class Solution:
    def reverseBits(self, n: int) -> int:
        # it is given in the constraints that the number is a 32 bit unsigned integer.
        # extract from the end and append to the start

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i)) # 31 because unsigned

        return res
