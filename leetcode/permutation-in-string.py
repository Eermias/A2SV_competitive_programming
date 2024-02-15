class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        countS1 = {}
        countS2 = {}
        l = 0
        r = len(s1) - 1

        for char in s1:
            countS1[char] = 1 + countS1.get(char, 0)
        

        for i in range(len(s1)):
            countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
        
        while r < len(s2):
            if countS1 == countS2:
                return True
            else:
                if countS2[s2[l]] == 1:
                    countS2.pop(s2[l])
                else:
                    countS2[s2[l]] -= 1
                l += 1
                r += 1
                if r == len(s2):
                    break
                countS2[s2[r]] = 1 + countS2.get(s2[r], 0)
        return countS1 == countS2

            
    
