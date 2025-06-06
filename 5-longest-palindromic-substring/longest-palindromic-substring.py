class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        
        longest = s[0]
        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j] and (j + 1 == i or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > len(longest):
                        longest = s[j : i + 1]
        
        return longest
