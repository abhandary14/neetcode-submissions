class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, opened, closed):
            if len(curr) >= 2*n: # length of complete parentheses
                res.append(curr)

            if opened < n: # there can be a max of n opening parentheses
                dfs(curr + "(", opened + 1, closed)
            if closed < opened: # there can be a max of 'opened' closing parentheses for it to be valid
                dfs(curr + ")", opened, closed + 1)
            
        dfs("", 0, 0)
        return res