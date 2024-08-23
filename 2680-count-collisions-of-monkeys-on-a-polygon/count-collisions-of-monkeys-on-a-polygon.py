class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(num):
            if num <= 1:
                return num + 1
            
            # important facts:
            # (a * b) % MOD == [(a % MOD) * (b % MOD)] % MOD
            # 2**n == 2**(n // 2) * 2**(n // 2) == (2**(n // 2)) ** 2 for even n
            # 2**n == 2 * (2**(n // 2)) ** 2 for odd n
            # (2**n) % MOD == (2**(n // 2) * 2**(n // 2)) % MOD == (a * b) % MOD 
            # where a == b == 2**(n // 2)
            # so (2**n) % MOD == (2**(n // 2) * 2**(n // 2)) % MOD == ((2**(n // 2) % MOD) ** 2) % MOD
            # so 2**n % MOD = ((2**(n // 2) % MOD) ** 2) % MOD
            # calculate temp = (2**(n // 2) % MOD) recursively and square it and take the modulo to MOD
            # to get 2**n % MOD.....for odd n you need to multiply by two

            temp = (power(num // 2) % (MOD))
            if num % 2 == 0:   
                return (temp**2) % (MOD)
            return (2 * ((temp**2) % (MOD))) % (MOD)

        return (power(n)-2) % (MOD)