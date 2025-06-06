class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 2)
        dp[-2] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue

            dp[i] += dp[i + 1]
            if '10' <= s[i : i + 2] <= '26':
                dp[i] += dp[i + 2]

        return dp[0]