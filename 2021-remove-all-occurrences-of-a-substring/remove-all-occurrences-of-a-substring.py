class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            if c == part[-1] and len(stack) >= len(part) - 1:
                found = True
                for i in range(-1, -len(part), -1):
                    if stack[i] != part[i - 1]:
                        found = False
                        break
                if found:
                    for i in range(len(part) - 1):
                        stack.pop()
                else:
                    stack.append(c)

            else:
                stack.append(c)

        return ''.join(stack)