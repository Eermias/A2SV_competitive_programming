class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for string in strs:
            common = common[:len(string)]
            for i in range(len(common)):
                if common[i] != string[i]:
                    common = common[:i]
                    break
            
        
        return common