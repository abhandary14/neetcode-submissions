class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # start from the last index

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal: # if from an index, we can reach goal or beyond it, then we can reach the goal from there and we now update the goal
                goal = i
        
        return goal == 0

