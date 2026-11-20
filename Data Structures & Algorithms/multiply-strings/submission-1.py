class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # we multiply like we multiplied on paper

        res = 0
        for i in range(len(num1)):
            ans = 0
            for j in range(len(num2)):
                d1 = int(num1[i]) * (10 ** (len(num1)-i-1))
                d2 = int(num2[j]) * (10 ** (len(num2)-j-1))

                ans += d1 * d2
            
            res += ans

        return str(res)
                 