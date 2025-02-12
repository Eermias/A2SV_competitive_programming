class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}

        for i in range(len(s)):
            dic[s[i]]=i
        
        last_position=0
        ans=[]
        start=0

        for i in range(len(s)):
            last_position=max(last_position,dic[s[i]])

            if i==last_position:
                ans.append(last_position-start+1)
                start=i+1
        
        return ans