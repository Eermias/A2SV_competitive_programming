class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ones = 0
        for n in s:
            if n == "1":
                ones += 1
            else:
                count += ones
        return count
        