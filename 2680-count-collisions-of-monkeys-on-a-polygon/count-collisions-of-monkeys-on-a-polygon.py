class Solution:
    def compute2Power(self, n):
        if n==1:
            return 2
        tmp=(self.compute2Power(n//2)%(1000000007))
        if n%2==0:   
            return (tmp**2)%(1000000007)
        return (2*((tmp**2)%(1000000007)))%(1000000007)

    def monkeyMove(self, n: int) -> int:
        return (self.compute2Power(n)-2)%(1000000007)