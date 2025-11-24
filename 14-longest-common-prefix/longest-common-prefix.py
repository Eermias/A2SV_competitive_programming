class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for word in strs:
            l, r = 0, 0
            while l < len(common) and r < len(word):
                if common[l] != word[r]:
                    break
                l += 1
                r += 1
            common = common[:l]
        
        return common