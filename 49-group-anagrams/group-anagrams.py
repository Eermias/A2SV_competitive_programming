class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            st = "".join(sorted(s))
            anagrams[st].append(s)
        
        return anagrams.values()