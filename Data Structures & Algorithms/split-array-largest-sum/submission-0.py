class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest: # 
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True

        l, r = max(nums), sum(nums) # if k = len(nums), the largest sum of any subarray would be the max of nums. if k = 1, the largest sum would be the sum. we search through this range to see if there's any split possible.
        res = r
        while l <= r:
            mid = l + (r-l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res