class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1

        # we calculate mid. if the array is rotated, then either left, or the right side of the array will be sorted.
        # we first check which side is sorted, and then search accordingly.

        while l <= r:
            mid = l + (r-l) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1