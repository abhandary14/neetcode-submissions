class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4 # target length of all sides
        sides = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False

        matchsticks.sort(reverse=True) # saving some time

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4): # only 4 sides
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    
                    if dfs(i + 1):
                        return True
                    
                    sides[j] -= matchsticks[i]

            return False
        
        return dfs(0)