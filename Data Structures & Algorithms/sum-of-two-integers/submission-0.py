class Solution:
    def getSum(self, a: int, b: int) -> int:
        # binary addition by XOR for the LSB (partial sum), and AND + left_shift for the carry

        carry = 0
        res = 0

        mask = 0xFFFFFFFF

        for i in range(32):
            # extract the bits
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2 # will give 0 or 1.

            if curr_bit:
                res |= (1 << i) 
            
        
        if res > 0x7FFFFFFF: # if it is larger than int max, then it is negative
            res = ~(res ^ mask)

        return res
