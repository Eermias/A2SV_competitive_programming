class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0 : -1}
        freq = defaultdict(int)

        longest = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            mask = 0
            for j, c in enumerate("aeiou"):
                if freq[c] % 2:
                    mask |= (1 << j)
            
            if mask in first:
                longest = max(longest, i - first[mask])
            else:
                first[mask] = i
        
        return longest
