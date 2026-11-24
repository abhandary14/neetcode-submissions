class Solution:
    def countBits(self, n: int) -> List[int]:
        # for every number count the bits
        # every number is a 32 bit integer

        res = []
        for num in range(n + 1):
            bit = 0
            for i in range(32):
                if num & (1 << i):
                    bit += 1
            
            res.append(bit)
        return res