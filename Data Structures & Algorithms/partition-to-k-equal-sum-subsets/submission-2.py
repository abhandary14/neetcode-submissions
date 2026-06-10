class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        nums.sort(reverse=True)
        
        if sum(nums) // k != target:
            return False
        
        used = [False] * len(nums) # tracking what numbers have been used

        def dfs(i, k, subsetSum):
            # two decisions. to include this current number or not.
            if k == 0:
                return True
            if subsetSum == target:
                return dfs(0, k-1, 0)

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True

                if dfs(j+1, k, subsetSum + nums[j]):
                    return True

                used[j] = False

            return False
        
        return dfs(0, k, 0)
                
