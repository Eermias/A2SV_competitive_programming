class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] + nums[:]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])
        
        return dp[-1]
