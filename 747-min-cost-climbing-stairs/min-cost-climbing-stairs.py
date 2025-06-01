class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {0:cost[0], 1:cost[1]} #base cases
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
            return memo[i]
        
        return dp(len(cost) - 1)