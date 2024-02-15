class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = ones = 0
        for c in s:
            if c == "1":
                ones += 1
            else:
                zeros += 1
        zeroPrefix = onePrefix = count = 0
        for c in s:
            if c == "0":
                count += onePrefix * (ones - onePrefix)
                zeroPrefix += 1
            else:
                count += zeroPrefix * (zeros - zeroPrefix)
                onePrefix += 1
        return count

         
        