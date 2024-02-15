class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashT = {}
        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)
        
        need = len(hashT)
        have = 0

        hashS = {}
        l = 0
        minn = ""
        minLen = float("infinity")
        for r in range(len(s)):
            c = s[r]
            hashS[c] = 1 + hashS.get(c, 0)
            if c in hashT:
                if hashS[c] == hashT[c]:
                    have += 1
            while have == need:
                if r - l + 1 < minLen:
                    minn = s[l:r+1]
                    minLen = r - l + 1
                c = s[l]
                hashS[c] -= 1
                l += 1
                if c in hashT and hashS[c] + 1 == hashT[c]:
                    have -= 1
        return minn
                


       

                

        

        

        

            
        
        