class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        stack = []
        for log in logs:
            if log == "../" and stack:
                stack.pop()
            elif log not in ["../", "./"]:
                stack.append(log)
        return len(stack)
        