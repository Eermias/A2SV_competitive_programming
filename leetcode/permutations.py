class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(added):
            if len(added) == len(nums):
                res.append(curr[:])
                return 
            
            for i in range(len(nums)):
                if i not in added:
                    curr.append(nums[i])
                    added.add(i)
                    dfs(added)
                    added.remove(i)
                    curr.pop()
        
        dfs(set())
        return res
            
        