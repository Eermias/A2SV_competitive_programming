class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        def is_valid(win, temp):
            for c in temp:
                if temp[c] > win[c]:
                    return False
            return True

        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1

        window = defaultdict(int)
        left = 0
        ans = [-1, -1]
        shortest = float('inf')
        for  right in range(len(s)):
            window[s[right]] += 1
            while is_valid(window, t_count):
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    ans = [left, right]

                window[s[left]] -= 1
                left += 1
        
        if ans[0] == -1:
            return ""
        else:
            return s[ans[0] : ans[1] + 1]
