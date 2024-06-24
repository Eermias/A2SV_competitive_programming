class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        maxlen = 0
        start = 0
        for i in range(N):
            seen = set()
            missing = 0
            for j in range(i, N):
                if s[j] not in seen: 
                    seen.add(s[j])
					
                    if (s[j].lower() not in seen) or (s[j].upper() not in seen):
                        missing += 1
                    else: 
                        missing -= 1
                if missing == 0 and (j - i + 1) > maxlen:
                    maxlen = j - i + 1
                    start = i
        return s[start:(start + maxlen)]