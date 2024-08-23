class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = 0
        split = []
        ops = []
        if expression[0] != '-':
            ops.append('+')

        for r in range(len(expression)):
            if expression[r] in "+-":
                split.append(expression[l: r])
                ops.append(expression[r])
                l = r + 1
        split.append(expression[l:])
        if split[0] == '':
            split = split[1:]
        
        denom = 1
        for fraction in split:
            idx = fraction.index('/') + 1
            denom *= int(fraction[idx:])
        
        numer = 0
        for i, fraction in enumerate(split):
            idx = fraction.index('/')
            top = int(fraction[:idx])
            bot = int(fraction[idx + 1:])
            if ops[i] == '+':
                numer += top * (denom // bot)
            else:
                numer -= top * (denom // bot)
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        gcdd = gcd(denom, abs(numer))
        denom //= gcdd
        numer //= gcdd

        return str(numer) + '/' + str(denom)


