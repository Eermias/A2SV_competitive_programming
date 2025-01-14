class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def count(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            
            memo[i] = count(i + 1)
            if i < n - 1 and s[i : i + 2] <= '26':
                memo[i] += count(i + 2)
            
            return memo[i]
        
        return count(0)