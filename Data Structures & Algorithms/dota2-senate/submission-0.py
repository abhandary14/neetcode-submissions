class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # we add indices of each senator in two separate queues for each party
        # then we take two out at a time and whoever is earlier doesn't get added back to the queue, denoting the end of their rights

        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == "D":
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if dTurn < rTurn:
                D.append(dTurn + n) # if they survive, they'll get to vote in the next round, so after dTurn + n turns
            else:
                R.append(rTurn + n)
        
        return "Dire" if D else "Radiant"