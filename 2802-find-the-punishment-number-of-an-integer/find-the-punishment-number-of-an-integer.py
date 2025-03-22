class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def backtrack(i, curr, num, ii):
            if i == len(num):
                if curr == ii:
                    return True
                return False
            
            temp = False
            for j in range(i + 1, len(num) + 1):
                temp = temp or backtrack(j, curr + int(num[i:j]), num, ii)
            return temp
            

        result = 0
        for i in range(1, n + 1):
            if backtrack(0, 0, str(i * i), i):
                result += i * i
        
        return result