class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # BROTHER IN CHRIST
        # find the starting point of a linked list cycle.
        # nums[i] points to the index nums[nums[i]]
        # so for example in nums = [1, 2, 3, 2, 2], each value nums[i] stores the next pointer
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow