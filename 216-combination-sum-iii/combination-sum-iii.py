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

"""class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(i, curr_sum):
            if len(curr) == k:
                if curr_sum == n:
                    result.append(curr[:])
                return 
            if i > 9:
                return
            
            curr.append(i)
            backtrack(i + 1, curr_sum + i)
            curr.pop()
            backtrack(i + 1, curr_sum)
        
        backtrack(1, 0)
        return result"""
            