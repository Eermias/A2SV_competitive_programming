class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        l, r = 0, len(x) - 1
        is_palindrome = True
        while l < r:
            if x[l] != x[r]:
                is_palindrome = False
                return is_palindrome
            l += 1
            r -= 1
        return is_palindrome
