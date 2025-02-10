class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for c in s:
            if c in '0123456789':
                result.pop()
            else:
                result.append(c)
        
        return ''.join(result)