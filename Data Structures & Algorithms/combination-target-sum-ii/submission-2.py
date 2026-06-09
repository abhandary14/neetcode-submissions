class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can choose the same value, but not the same combination.
        res = []

        # we can sort and skip
        candidates.sort()

        def dfs(i, curr, total):
            # the 'curr not in res' is giving a TLE
            if total == target:
                res.append(curr[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            

            # include
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            # in the case where we're not including it, we can skip duplicates.
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res