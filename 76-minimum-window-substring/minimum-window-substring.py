class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1

        window = defaultdict(int)
        left = 0
        ans = [-1, -1]
        shortest = float('inf')
        valid_count = 0
        for  right in range(len(s)):
            window[s[right]] += 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                valid_count += 1

            while valid_count == len(t_count):
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    ans = [left, right]

                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    valid_count -= 1

                left += 1
        
        if ans[0] == -1:
            return ""
        else:
            return s[ans[0] : ans[1] + 1]
