class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for c in s1:
            map1[c] = 1 + map1.get(c, 0)

        map2 = {}
        l = 0
        for r in range(len(s2)):
            map2[s2[r]] = 1 + map2.get(s2[r], 0)
            
            if r - l + 1 > len(s1):
                map2[s2[l]] -= 1
                if map2[s2[l]] == 0:
                    map2.pop(s2[l])
                l += 1
            if map1 == map2:
                return True
        
        return False
        