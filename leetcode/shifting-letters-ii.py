class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftPrefix = [0]*len(s)
        for l,r,dxn in shifts:
            shiftPrefix[l] += 1 if dxn == 1 else -1

            if r+1 < len(s):
                shiftPrefix[r+1] -= 1 if dxn == 1 else -1
        for i in range(1,len(s)):
            shiftPrefix[i] += shiftPrefix[i-1]

        res = ""
        for i,c in enumerate(s):
            shift = shiftPrefix[i] % 26
            if (ord(c) + shift) > ord('z'):
                n = shift - (ord('z') - ord(c))
                res += chr(ord('a') + n - 1)
            else:
                res += chr(ord(c) + shift)
        return res
            
             
            
            

        

        