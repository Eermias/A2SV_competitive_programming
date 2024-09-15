class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0 : -1}
        vowels = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}

        longest = 0
        mask = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= (1 << vowels[c])
            
            if mask in first:
                longest = max(longest, i - first[mask])
            else:
                first[mask] = i
        
        return longest
