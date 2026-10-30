class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # stone game 2, but fix "X" to 3

        # when alice takes a pile, we increase a 'score' variable
        # when bob takes a pile, we decrease a 'score' variable
        # 'score' stores the difference in scores between alice and bob.
        # if at the end it is positive, alice wins, else bob wins

        n = len(stoneValue)
        memo = {}

        # i -> current index, alice is a bool indicating whose turn it is
        def dfs(i, alice):
            if i >= n:
                return 0
            if (i, alice) in memo:
                return memo[(i, alice)]
            
            res = float('-inf') if alice else float('inf') # if it is alice's turn, we're she's trying to maximize her score, and if it is bob's turn, he's trying to minimize her score

            score = 0

            # i + 3 needs to be in bounds
            # make sure j starts from i ****
            for j in range(i, min(i + 3, n)):
                if alice:
                    score += stoneValue[j]
                    res = max(res, score + dfs(j + 1, not alice))
                else:
                    score -= stoneValue[j]
                    res = min(res, score + dfs(j + 1, not alice))
                
            memo[(i, alice)] = res
            return res
        
        res = dfs(0, 1)
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"