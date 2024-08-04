class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0] * 26
        
        longest = 0
        l = 0
        for r in range(len(s)):
            window[ord(s[r]) - ord("A")] += 1
            while (r - l + 1) - max(window) > k:
                window[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest