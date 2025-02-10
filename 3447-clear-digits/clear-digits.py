class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        removed = [False] * n
        for i in range(n):
            if s[i] in '0123456789':
                removed[i] = True
                for j in range(i - 1, -1, -1):
                    if s[j] not in '0123456789' and not removed[j]:
                        removed[j] = True
                        break
        
        result = []
        for i in range(n):
            if not removed[i]:
                result.append(s[i])
        
        return ''.join(result)