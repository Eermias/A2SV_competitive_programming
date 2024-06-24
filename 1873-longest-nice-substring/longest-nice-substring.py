class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def longest(l, r):
            if l > r:
                return ""
            
            letters = set()
            for c in s[l : r + 1]:
                letters.add(c)
            
            for i in range(l, r + 1):
                if s[i].lower() not in letters or s[i].upper() not in letters:
                    left = longest(l, i - 1)
                    right = longest(i + 1, r)
                    if len(left) >= len(right):
                        return left
                    return right
            
            return s[l : r + 1]
        
        return longest(0, len(s) - 1)