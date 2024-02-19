class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+","-","*","/"}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if t == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop()
                elif t == "-":
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop()
                elif t == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop()
                else:
                    res = stack[-2]//stack[-1]
                    stack[-2] = res if res>=0 or stack[-2]%stack[-1]==0 else res+1
                    stack.pop()
        return stack[-1]
                

        