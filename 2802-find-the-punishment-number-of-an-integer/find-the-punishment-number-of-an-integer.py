class Solution:
    def punishmentNumber(self, n: int) -> int:
            
        options = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        return sum(num**2 for num in options if num <= n)