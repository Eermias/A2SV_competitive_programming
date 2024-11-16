class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = 0
        for i in range(1, len(str2) + 1):
            gcd = str2[:i]
            if len(str1) % i:
                continue
            okay = True
            for j in range(0, len(str1), i):
                if str1[j : j + i] != gcd:
                    okay = False
                    break

            for j in range(0, len(str2), i):
                if str2[j : j + i] != gcd:
                    okay = False
                    break

            if okay:
                ans = i
        
        return str2[:ans]

