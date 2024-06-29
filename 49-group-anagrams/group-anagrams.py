class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            st = sorted(s)
            anagrams[tuple(st)].append(s)
        
        return anagrams.values()