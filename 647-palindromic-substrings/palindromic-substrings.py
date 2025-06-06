class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j):
            l, r = i, j
            count = 0
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i + 1)
        
        return ans