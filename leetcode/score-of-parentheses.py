class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [""]
        score = [0]
        for c in s:
            if c == "(":
                stack.append("(")
                score.append(0)
            else:
                if score[-1] == 0:
                    score[-2] += 1
                else:
                    score[-2] += 2 * score[-1]
                stack.pop()
                score.pop()
        return score[-1]


        