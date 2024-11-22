class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = set(['+', '-', '*'])
        def compute(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            else:
                return a * b
        
        def backtrack(l, r):
            res = []
            for i in range(l, r):
                op = expression[i]
                if op in operators:
                    left = backtrack(l, i)
                    right = backtrack(i + 1, r)
                
                    for n1 in left:
                        for n2 in right:
                            res.append(compute(n1, n2, op))
            
            if not res:
                res.append(int(expression[l : r]))
            
            return res
        
        return backtrack(0, len(expression))