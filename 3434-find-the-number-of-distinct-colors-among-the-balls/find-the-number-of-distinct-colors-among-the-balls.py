class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        colors = defaultdict(int)
        ans = []
        curr = 0
        for x, y in queries:
            if colors[x] == y:
                ans.append(curr)
            else:
                count[colors[x]] -= 1
                if count[colors[x]] == 0:
                    curr -= 1

                colors[x] = y
                count[y] += 1
                if count[y] == 1:
                    curr += 1
                
                ans.append(curr)
                
        return ans




