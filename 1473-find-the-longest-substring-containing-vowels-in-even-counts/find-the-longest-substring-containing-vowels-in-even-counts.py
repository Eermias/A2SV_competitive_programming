class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prev = {0 : -1}
        freq = defaultdict(int)

        longest = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            mask = 0
            for j, c in enumerate("aeiou"):
                if freq[c] % 2:
                    mask |= (1 << j)
            
            if mask in prev:
                longest = max(longest, i - prev[mask])
            else:
                prev[mask] = i
        
        return longest
