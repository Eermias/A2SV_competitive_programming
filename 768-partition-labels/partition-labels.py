class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        last = 0
        part = []
        for i in range(len(s)):
            count[s[i]] -= 1
            okay = True
            for j in range(last, i + 1):
                if count[s[j]] != 0:
                    okay = False
                    break
            
            if okay:
                part.append(i - last + 1)
                last = i + 1
        
        return part

        