class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(num, total, count):
            if count == k or total > n:
                if total == n:
                    res.append(curr[:])
                return
            for i in range(num, 10):
                curr.append(i)
                dfs(i + 1, total + i, count + 1)
                curr.pop()
        dfs(1, 0, 0)
        return res

