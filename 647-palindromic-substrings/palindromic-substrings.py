class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        #mark every single letter as a palindrome
        for i in range(n):
            dp[i][i] = True
        
        count = n
        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j] and (dp[j + 1][i - 1] == True or j + 1 == i):
                    dp[j][i] = True
                    count += 1
        
        return count