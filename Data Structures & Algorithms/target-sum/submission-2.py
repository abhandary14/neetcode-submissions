# so, our DP table will look like this:
# for nums = [1, 1, 1, 1, 1], target = 3
# each row corresponds to the number of elements we have selected from the array
# each column represents the sum possible using the given elements
# the value dp[i][curr_sum] = number of ways to sum up to curr_sum, given we have selected the first i values from nums.
# the base case is: if we have no elements, and our target is 0, then we have 1 way of making 0 using no elements.
# dp[0][0] = 1
# now from there, we can build up the DP table using the result of the previous row
# so if we take 1 element, then our curr_sum in this case can only be 1 and -1
# then if we take 2 elements, then our curr_sum can be -1-1 = -2, -1+1 = 0, 1-1 = 0, 1+1 = 2. so 1 way to go to -2 and 2, and 2 ways to go to 0... and so on and so forth
#   -5 -4 -3 -2 -1  0  1  2  3  4  5
# 0[                1               ]
# 1[             1     1            ]
# 2[          1     2     1         ]
# 3[                                ]
# 4[                                ]
# 5[                                ]

# our result will be stored in dp[n][target]
# we should use a dictionary to store each row's results. the key will be the current achievable sum, and the value will be the count.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [defaultdict(int) for _ in range(n+1)]
        # key = curr_sum, val = count
        
        dp[0][0] = 1 # 0 elements, target = 0 -> 1 way to achieve

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        
        return dp[n][target]
