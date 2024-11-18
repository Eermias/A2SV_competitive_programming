class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = []
        for c in s:
            if stack and stack[-1] == c:
                if count[-1] == k - 1:
                    while stack and stack[-1] == c:
                        stack.pop()
                        count.pop()
                else:
                    stack.append(c)
                    count.append(count[-1] + 1)
            else:
                stack.append(c)
                count.append(1)
        
        return ''.join(stack)
