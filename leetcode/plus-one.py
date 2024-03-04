class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for n in digits:
            res += str(n)
        res= str(int(res) + 1)
        ans = [int(x) for x in list(res)]

        return ans

          
        