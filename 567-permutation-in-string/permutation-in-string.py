class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        same = 0
        for i in range(26):
            if count1[i] == count2[i]:
                same += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if same == 26:
                return True
            
            count2[ord(s2[r]) - ord('a')] += 1
            if count2[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')]:
                same += 1
            elif count2[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')] + 1:
                same -= 1
            
            count2[ord(s2[l]) - ord('a')] -= 1
            if count2[ord(s2[l]) - ord('a')] == count1[ord(s2[l]) - ord('a')]:
                same += 1
            elif count2[ord(s2[l]) - ord('a')] + 1 == count1[ord(s2[l]) - ord('a')]:
                same -= 1
            l += 1
        
        return same == 26
            