class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            map1 = {}
            map2 = {}
            for i in range(len(pattern)):
                map1[word[i]] = pattern[i]
                map2[pattern[i]] = word[i]
            
            #print(map1)
            okay = True
            for i, c in enumerate(word):
                if map1[c] != pattern[i] or map2[pattern[i]] != c:
                    okay = False
            
            if okay:
                result.append(word)
        
        return result