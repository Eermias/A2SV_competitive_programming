class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        ans = ['0']
        #read white space
        while i < len(s) and s[i] == " ":
            i += 1
        #read sign
        is_positive = True
        if i < len(s) and s[i] == '-':
            is_positive = False
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        #read numbers and terminate when any non-digit character is found
        digits = "0123456789"
        while i < len(s) and s[i] in digits:
            ans.append(s[i])
            i += 1

        #compute the result
        res = int(''.join(ans))
        if not is_positive:
            res *= -1
        
        #round to get a numbers in the 32-bit range
        if res < -2**31:
            res = -2**31
        elif res > 2**31 - 1:
            res = 2**31 - 1
        
        return res