# In each turn, we have multiple choices. 
# - take 1st pile, take first two piles, ... take first X piles
# - if both players play optimally, then both will try and increase their score to the max by trying out all possibilities.
# - that means we'd have to store both of their scores, and that'd make things very complicated.
# - So instead, what we can do is only track alice's score. When it is alice's turn, we try to maximize her score
# - When it is bob's turn, we try to minimize alice's score.

# O(n^3) -> damn
# O(n^2)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # we only store alice's score
        # when it is alice's turn, we try to maximize her score
        # when it is bob's turn, we try to minimize alice's score.

        # returns the number of stones alice can get.
        # i = index in the piles, and M is used to calculate X

        dp = {} # (alice?, i, and M) -> stores alice's max score

        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]
            
            res = 0 if alice else float('inf')
            
            # prefix so that we don't have to write a separate loop to try all posibilities of X
            prefix = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles): # the number of piles to take must be in bounds
                    break

                prefix += piles[i + X - 1] # prefix sum

                if alice:
                    # maximize her score by taking piles
                    res = max(res, prefix + dfs(not alice, i + X, max(M, X)))
                else:
                    # minimize her score, and she can't take piles in this case
                    res = min(res, dfs(not alice, i + X, max(M, X)))

            dp[(alice, i, M)] = res
            return res
        
        return dfs(alice=True, i=0, M=1)
