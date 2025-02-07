class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(2**31))
        
        while a <= b and a**2 + b**2 != c:
            if a**2 + b**2 < c:
                a += 1
            else:
                b -= 1
        
        return True if a <= b else False