class Solution:
    # worst case time complexity O(n)
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True
            
            if nums[l] < nums[mid]: # we're in the left part
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[l] > nums[mid]: # we're in the right part
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else: # we just add this else case if l is nums[mid], then skip till it isn't (linear)
                l += 1
        
        return False
