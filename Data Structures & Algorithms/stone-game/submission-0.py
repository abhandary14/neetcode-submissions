class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # there are even number of piles in the list
        # whenever it is Alice's turn, there will be even number of piles as she goes first.
        
        memo = [[None] * len(piles) for _ in range(len(piles))]

        def dfs(l, r): # dfs(l, r) returns Alice's maximum score for piles[l:r+1]
            if l > r:
                return 0
            if memo[l][r] is not None:
                return memo[l][r]
            
            # it is alice's turn when (r - l) is even
            # either left or right and we add to the score
            # recurse and take max of left, right

            even = (r - l) % 2 == 0

            left = piles[l] if even else 0
            right = piles[r] if even else 0

            memo[l][r] = max(left + dfs(l + 1, r), right + dfs(l, r-1)) 
            return memo[l][r]
        

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score
