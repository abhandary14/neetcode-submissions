class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # bruteforce: O(n * m), n is the length of smallest string, m is the number of strings.
        # ans = ""
        # smallest = strs[0]
        # for s in strs:
        #     if len(s) < len(smallest):
        #         smallest = s
        
        # for i in range(len(smallest)):
        #     for word in strs:
        #         if smallest[i] != word[i]:
        #             return ans
        #     ans += smallest[i]
        
        # return ans

        # optimized - we will sort the list in nlogn time, then compare the first and last words only. if there is a common prefix, it should be correct
        strs.sort()
        ans = ""

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
            else:
                break
            
        return ans