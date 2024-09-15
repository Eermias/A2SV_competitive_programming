class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prev = {(0, 0, 0, 0, 0) : -1}
        freq = defaultdict(int)

        longest = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            pattern = [0] * 5
            for j, c in enumerate("aeiou"):
                if freq[c] % 2:
                    pattern[j] = 1
            
            if tuple(pattern) in prev:
                longest = max(longest, i - prev[tuple(pattern)])
            else:
                prev[tuple(pattern)] = i
        
        return longest
