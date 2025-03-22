class Solution:
    def punishmentNumber(self, n: int) -> int:
        self.ans = 0
        def backtrack(num, indx, k):
            if indx >= len(num):
                if k == 0:
                    self.ans += int(num)
                    return True
                return False
            for i in range(indx, len(num)):
                curr = num[indx:i+1]
                k -= int(curr)
                
                if backtrack(num, i+1, k):
                    return True
                k += int(curr)
            # return False

        for i in range(1, n+1):
            backtrack(str(i*i), 0, i)
        return self.ans
