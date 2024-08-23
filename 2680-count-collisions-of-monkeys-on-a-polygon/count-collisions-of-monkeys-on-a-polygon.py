class Solution:
    def monkeyMove(self, n: int) -> int:
        res = pow(2, n, 10**9 + 7) - 2
        return res % (10**9 + 7)