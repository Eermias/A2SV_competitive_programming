class Solution:
    def splitNum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        num1, num2 = [], []
        for i, n in enumerate(nums):
            if i % 2:
                num1.append(n)
            else:
                num2.append(n)
        
        return int("".join(num1)) + int("".join(num2))