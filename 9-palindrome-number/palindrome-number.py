class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        digits = []
        while x:
            digits.append(x % 10)
            x //= 10
        
        return digits == digits[::-1]
