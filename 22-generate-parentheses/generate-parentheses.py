class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(par):
            stack = []
            for br in par:
                if br == "(":
                    stack.append("(")
                else:
                    if not stack:
                        return False
                    stack.pop()
            return True if not stack else False

        combinations = []
        def generate(n, comb):
            if n == 0:
                if isValid(comb):
                    combinations.append(comb)
                return
            generate(n - 1, comb + '(')
            generate(n - 1, comb + ')')
        
        generate(2 * n, "")
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