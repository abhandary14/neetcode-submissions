class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001

        for t in trips:
            numPass, s, e = t
            passChange[s] += numPass
            passChange[e] -= numPass
        
        currPass = 0
        for i in range(1001):
            currPass += passChange[i]
            if currPass > capacity:
                return False
        return True
