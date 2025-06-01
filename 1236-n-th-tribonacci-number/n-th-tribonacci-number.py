class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return min(n, 1)
        
        one, two, three = 0, 1, 1
        for i in range(3, n + 1):
            temp = one + two + three
            one = two
            two = three
            three = temp
        
        return three