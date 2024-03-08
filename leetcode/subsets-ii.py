class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        curr = []
        def dfs(idx):
            if idx == len(nums):
                if tuple(curr) not in res:
                    res.add(tuple(curr[:]))
                return
            curr.append(nums[idx])
            dfs(idx + 1)
            curr.pop()
            dfs(idx + 1)

        dfs(0)
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        
        return res
        