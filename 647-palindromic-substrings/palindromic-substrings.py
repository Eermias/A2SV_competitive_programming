class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        palindromes = n
        for i in range(1, n):
            for j in range(i):
                if s[j] == s[i] and (i == j + 1 or dp[j + 1][i - 1]):
                    palindromes += 1
                    dp[j][i] = True
        
        return palindromes