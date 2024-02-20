class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #basecase
        if n == 1: return True
        if n < 1: return False

        #function calling itself with cange in state
        return self.isPowerOfFour(n/4)
        