class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # we multiply like we multiplied on paper

        if num1 == "0" or num2 == "0":
            return "0"
        
        # the number of digits in results can be at max the sum of digits in num1 and num2
        res = [0] * (len(num1) + len(num2))

        # we multiply like on paper from right to left
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1 + i2]     += int(num1[i1]) * int(num2[i2]) # add
                res[i1 + i2 + 1] += res[i1 + i2] // 10 # carry over
                res[i1 + i2]     %= 10 # normalize to single digit
        
        # we need to get rid of leading zeros
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # make every value in there a string, then join it
        return "".join(map(str, res[beg:]))