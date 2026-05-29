class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if len(height)==0:
            return 0

        prefix = [0] * len(height)
        suffix = [0] * len(height)

        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix[i-1])

        suffix[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(height[i], suffix[i+1])

        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i] 
        
        return water