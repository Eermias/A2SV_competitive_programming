class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def poww(base, exp):
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                return poww((base*base) % mod, exp//2)
            else:
                return base * poww((base*base) % mod, (exp - 1)//2)
        even = ceil(n/2)
        odd = floor(n/2)

        res = poww(5, even) % mod * poww(4, odd) % mod
        return res % (10**9 + 7)

        
        