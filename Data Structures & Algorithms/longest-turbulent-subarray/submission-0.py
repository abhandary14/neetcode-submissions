class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # bruteforce would be to go through all subarrays and check turbulence

        # to optimize this, we use a variable sized sliding window

        l, r = 0, 1
        res = 1
        prev = "" # previous comparison sign result

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r-1] else r # skip the equal numbers
                l = r - 1 # update l to just before r. this is because a subarray of a turbulent array is also a turbulent array. so we don't need to check every l position
                prev = ""
        
        return res


