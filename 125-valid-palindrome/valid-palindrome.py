class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alpha(c):
            if (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                c in "0123456789"):
                return True
            return False

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not is_alpha(s[l]):
                l += 1
            while r > l and not is_alpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True