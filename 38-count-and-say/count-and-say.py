class Solution:
    def countAndSay(self, n: int) -> str:
        def say(s):
            temp = []
            count = 0 
            for i in range(len(s)):
                count += 1
                if i == len(s) - 1 or s[i] != s[i + 1]:
                    temp.append(str(count))
                    temp.append(s[i])
                    count = 0

            return ''.join(temp)

        ans = '1'
        for _ in range(n - 1):
            ans = say(ans)
        
        return ans