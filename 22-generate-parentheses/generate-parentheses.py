class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        stack = []
        def generate(open, close):
            if open == close == n:
                combinations.append("".join(stack))
                return
            if open > close:
                stack.append(')')
                generate(open, close + 1)
                stack.pop()
            if open < n:
                stack.append('(')
                generate(open + 1, close)
                stack.pop()
        generate(0, 0)
        return combinations


























        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res