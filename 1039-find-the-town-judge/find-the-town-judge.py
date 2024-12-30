class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [[0, 0] for _ in range(n)] # [in, out]
        for a, b in trust:
            degree[a - 1][1] += 1
            degree[b - 1][0] += 1
        
        for i in range(n):
            if degree[i][0] == n - 1 and degree[i][1] == 0:
                return i + 1
        return -1