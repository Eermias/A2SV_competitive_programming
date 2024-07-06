class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (2 * (n - 1))
        left = time - rounds * 2 * (n - 1)
        if left > n - 1:
            left -= n - 1
            return n - left
        return 1 + left