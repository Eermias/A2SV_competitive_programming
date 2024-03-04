class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
        




        #WEAK, this is cheating 
        """res = ""
        for n in digits:
            res += str(n)
        res= str(int(res) + 1)
        ans = [int(x) for x in list(res)]

        return ans"""

          
        