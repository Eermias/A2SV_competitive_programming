class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                return
            subset.append(nums[i])
            res.append(subset.copy())
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res + [[]]


        