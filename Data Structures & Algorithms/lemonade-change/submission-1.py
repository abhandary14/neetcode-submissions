class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # we can only pay them back using $5 and $10 bills cause the maximum change we return to anyone is $15 (5 + 10), when they give a 20
        # so we keep a count of $5 and $10 bills
        # if they give a tenner, we need to give back 5, so we decrement 5 count and increase 10 count since we just gained a tenner.
        # if they give a 20, prefer using one 10 + one 5. if not 10, use three 5s. 
        # return False if none of this works

        five, ten = 0, 0

        for bill in bills:
            # if they give a fiver, then increment the count
            if bill == 5:
                five += 1
            
            # if they give a tenner, increment ten count, but check if we can give 5 back or no
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False

            # if they give 20, then
            else:
                change = bill - 5
                # check if we have both fives and tens, then give back one five and one ten
                if change == 15 and five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                # else try to give 3 fives
                elif change == 15 and five >= 3:
                    five -= 3
                else:
                    return False

        return True