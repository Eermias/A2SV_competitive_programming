class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False




        stack = []
        for p in s:
            if p == "[" or p == "{" or p== "(":
                stack.append(p)
            else:
                if p == "]":
                    if not stack:
                        return False
                    elif stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif p == "}":
                    if not stack:
                        return False
                    elif stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    if not stack:
                        return False
                    elif stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
        return True if not stack else False
        