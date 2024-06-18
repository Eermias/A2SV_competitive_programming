class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l >= r:
                return 1
            
            count = 0
            for i in range(l, r + 1):
                count += dp(l, i - 1) * dp(i + 1, r)
            memo[(l, r)] = count
            return count

        
        return dp(1, n)
