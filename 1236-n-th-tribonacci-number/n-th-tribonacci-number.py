class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        if n in memo:
            return memo[n]
        
        one, two, three = 0, 1, 1
        for i in range(3, n + 1):
            temp = one + two + three
            one = two
            two = three
            three = temp
        
        return three