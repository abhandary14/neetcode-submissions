class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:]) # return the permutations without the first element. so every time we're dividing this into subproblems where nums keeps getting smaller and smaller
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res