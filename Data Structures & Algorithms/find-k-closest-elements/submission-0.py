class Solution:
    # def searchInsert(self, arr: List[int], x: int) -> int:
    #     l, r = 0, len(arr)-1

    #     while l <= r:
    #         mid = l + (r-l) // 2 

    #         if target == arr[mid]:
    #             return mid
    #         elif target > arr[mid]:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #         return l


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            mid = l + (r-l) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid
            else:
                l = mid + 1
        
        return arr[l:l+k]
