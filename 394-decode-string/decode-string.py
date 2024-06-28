class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = "0123456789"
        for c in s:
            stack.append(c)
            if c == ']':
                stack.pop()
                encoded = ""
                while stack[-1] != '[':
                    encoded = stack.pop() + encoded

                stack.pop()
                multiplier = ""
                while stack and stack[-1] in digits:
                    multiplier = stack.pop() + multiplier
                
                stack.append(int(multiplier) * encoded)
        
        return "".join(stack)