class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = s.split()
        maxx = 0
        for i in range(len(s)):
            maxx = max(maxx, len(s[i]))
        

        ans = [[] for _ in range(maxx)]
        for i in range(maxx):
            for word in s:
                if i < len(word):
                    ans[i].append(word[i])
                else:
                    ans[i].append(" ")
        
        for i in range(maxx):
            while ans[i][-1] == " ":
                ans[i].pop()

            ans[i] = "".join(ans[i])
        
        return ans

        