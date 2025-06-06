class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        def expand(i, j):
            nonlocal longest
            
            l, r = i, j
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if r - l - 1 > len(longest):
                longest = s[l + 1 : r]
            
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return longest