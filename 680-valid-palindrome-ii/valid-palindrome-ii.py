class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                option1 = s[:l] + s[l + 1:]
                option2 = s[:r] + s[r + 1:]
                return option1 == option1[::-1] or option2 == option2[::-1]
        
        return True
