class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # there are even number of piles in the list
        # whenever it is Alice's turn, there will be even number of piles as she goes first.
        
        dp = [[0] * len(piles) for _ in range(len(piles))]

        for l in range(len(piles)-1, -1, -1):
            for r in range(l, len(piles)):
                even = (r - l) % 2 == 0
                left = piles[l] if even else 0
                right = piles[r] if even else 0

                if l == r:
                    dp[l][r] = left
                
                else:
                    dp[l][r] = max(left + dp[l + 1][r], right + dp[l][r-1])

        total = sum(piles)
        alice_score = dp[0][-1]

        return alice_score > total - alice_score