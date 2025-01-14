class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = s[0]
        for l in range(len(s)):
            for r in range(len(s) - 1, l - 1, -1):
                if check(l, r):
                    if r - l + 1 > len(ans):
                        ans = s[l : r + 1]
                    break
        return ans

