class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 # can't complete the circuit no matter what

        total = 0 # total amount in the tank at any given time
        res = 0 # candidate index

        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # add remaining gas to the tank

            if total < 0: # if total becomes negative, then this position can't be our 
                total = 0
                res = i + 1 # so we set the total to 0 and set the next index a candidate
        
        return  res
