# Copied from leetcode ->
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # we need to find where the array switches it's direction (peak)
        # then we can run binary search on both sides

        # 2, 4, 5, 3, 2, 1 -> peak is not in the middle, so we need to do binary search to find peak

        # finding the peak
        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m


        # search left position
        # all elements left of the peak are sorted in ascending order
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # search right position
        # all elements right of the peak are sorted in descending order
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m
        
        return -1
                