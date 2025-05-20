class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if i == len(s):
                if p[j] == '*' or (j + 1 < len(p) and p[j + 1] == '*'):
                    memo[(i, j)] = match(i, j + 1)
                    return memo[(i, j)]
                return False
            if j >= len(p):
                return False

            if p[j] == s[i]:
                if match(i + 1, j + 1):
                    memo[(i, j)] = True
                    return True
                if j + 1 < len(p) and p[j + 1] == '*' and match(i, j + 2):
                    memo[(i, j)] = True
                    return True
                memo[(i, j)] = False
                return False

            if p[j] == '.':
                if match(i + 1, j + 1):
                    return True
                if j + 1 < len(p) and p[j + 1] == '*':
                    if match(i, j + 1):
                        memo[(i, j)] = True
                        return True
                    memo[(i, j)] = False
                    return False

                memo[(i, j)] = False
                return False

            if p[j] == '*':
                if match(i, j + 1):
                    memo[(i, j)] = True
                    return True

                c = p[j - 1]
                for k in range(i - 1, len(s)):
                    if c == '.' or c == s[k]:
                        if match(k + 1, j + 1):
                            memo[(i, j)] = True
                            return True
                    else:
                        memo[(i, j)] = False
                        return False
                memo[(i, j)] = False
                return False

            
            if p[j] != s[i]:
                if j + 1 < len(p) and p[j + 1] == '*' and match(i, j + 2):
                    memo[(i, j)] = True
                    return True
                memo[(i, j)] = False
                return False
        
        return match(0, 0)
    
            
