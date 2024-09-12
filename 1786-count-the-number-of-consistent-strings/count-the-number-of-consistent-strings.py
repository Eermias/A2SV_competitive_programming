class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        pattern = [0] * 26
        for c in allowed:
            pattern[ord(c) - ord('a')] = 1
        
        count = 0
        for word in words:
            curr = [0] * 26
            for c in word:
                curr[ord(c) - ord('a')] = 1
            
            valid = True
            for i in range(26):
                if curr[i] == 1 and pattern[i] != 1:
                    valid = False
            
            if valid:
                count += 1
        
        return count
