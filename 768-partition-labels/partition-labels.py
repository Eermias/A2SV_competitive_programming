class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        
        last_pos = 0
        start = -1
        parts = []
        for i in range(len(s)):
            last_pos = max(last_pos, dic[s[i]])
            if last_pos == i:
                parts.append(i - start)
                start = i
        
        return parts
