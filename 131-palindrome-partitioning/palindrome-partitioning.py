class Solution:
    def partition(self, s: str) -> List[List[str]]:
        valid_ways = []
        curr = []
        def dfs(i):
            if i == len(s):
                valid_ways.append(curr[:])
                return
            
            for j in range(i + 1, len(s) + 1):
                part = s[i : j]
                if part == part[::-1]:
                    curr.append(part)
                    dfs(j)
                    curr.pop()
                    
        dfs(0)
        return valid_ways