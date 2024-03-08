class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(idx):
            if len(curr) == k:
                res.append(curr[:])
                return
            if idx == n:
                return
            
            curr.append(idx + 1)
            dfs(idx + 1)
            curr.pop()
            dfs(idx + 1)

        dfs(0)
        return res
        