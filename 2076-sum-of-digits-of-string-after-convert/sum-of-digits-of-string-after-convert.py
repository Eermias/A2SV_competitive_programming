class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = [""] * len(s)
        for j, c in enumerate(s):
            temp[j] = str(ord(c) - ord('a') + 1)
        s = "".join(temp)

        for i in range(k):
            summ = 0
            for c in s:
                summ += int(c)
            s = str(summ)
        
        return int(s)