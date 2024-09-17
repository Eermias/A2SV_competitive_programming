class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        map1 = defaultdict(int)
        for word in s1:
            map1[word] += 1
        
        map2 = defaultdict(int)
        for word in s2:
            map2[word] += 1
        
        uncommon = []
        for word in map1:
            if map1[word] == 1 and word not in map2:
                uncommon.append(word)
        
        for word in map2:
            if map2[word] == 1 and word not in map1:
                uncommon.append(word)
        
        return uncommon