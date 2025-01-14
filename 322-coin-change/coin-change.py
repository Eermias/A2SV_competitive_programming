class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        memo = {}
        def check(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if curr == amount:
                return 0
            if i == n or amount < curr:
                return float('inf')
            
            pick = 1 + check(i, curr + coins[i])
            skip = check(i + 1, curr)

            memo[(i, curr)] = min(pick, skip)
            return memo[(i, curr)]
        
        res = check(0, 0)
        if res == float('inf'):
            res = -1
        
        return res
            
