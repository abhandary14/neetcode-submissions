class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # we can only pay them back using $5 and $10 bills cause the maximum change we return to anyone is $15 (5 + 10), when they give a 20
        # so we keep a count of $5 and $10 bills
        # if they give a tenner, we need to give back 5, so we decrement 5 count and increase 10 count since we just gained a tenner.
        # if they give a 20, prefer using one 10 + one 5. if not 10, use three 5s. 
        # return False if none of this works

        # a simplification is to just perform operations on fives and tens, and then check if the five count at the end if negative. It should not be negative

        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            
            if five < 0:
                return False
        
        return True
    