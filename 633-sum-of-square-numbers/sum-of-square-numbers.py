class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(2**31))
        
        while a <= b:
            product = a**2 + b**2
            if product == c:
                return True

            if product < c:
                a += 1
            else:
                b -= 1
        
        return False