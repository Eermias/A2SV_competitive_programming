class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ")":
                stack.append(c)
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
        
        return "".join(stack)