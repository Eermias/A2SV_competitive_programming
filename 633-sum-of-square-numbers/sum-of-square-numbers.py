class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        prime_factors = []
        
        if c == 0:
            return True

        while c % 2 == 0:
            prime_factors.append(2)
            c /= 2
        
        for i in range(3, int(sqrt(c)) + 1, 2):
            while c % i == 0:
                prime_factors.append(i)
                c /= i
        
        if c >= 2:
            prime_factors.append(int(c))
        is_sum = True
        for p in prime_factors:
            if p % 4 == 3:
                if prime_factors.count(p) % 2 == 1:
                    is_sum = False
        
        return is_sum