class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        dp = cost[:]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return dp[-1]