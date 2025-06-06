class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 4)
        dp[0] = 0

        for i in range(amount):
            if dp[i] != float('inf'):
                for c in coins:
                    if i + c <= amount:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1