class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = defaultdict(int)
        l, longest = 0, 0
        for r in range(len(s)):
            prev[s[r]] += 1
            while prev[s[r]] > 1:
                prev[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest
        