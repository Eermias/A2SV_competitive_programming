class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1} #base case
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)
        