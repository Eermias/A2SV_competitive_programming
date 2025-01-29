class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        original = x
        
        while x:
            reverse += (x % 10)
            reverse *= 10
            x //= 10
        
        return reverse // 10 == original
