class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0: #should be flipped
            return self.kthGrammar(n - 1, k // 2) ^ 1
        else:
            return self.kthGrammar(n - 1, (k + 1) // 2)


        """if n == 1:
            return 0
        x = 2 ** (n - 2)
        if k > x:
            return 1 ^ self.kthGrammar(n - 1, k - x)
        return self.kthGrammar(n - 1, k)"""