class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        sub_set = []
        def backtrack(i):
            if i == len(nums):
                power_set.append(sub_set[:])
                return
            
            sub_set.append(nums[i])
            backtrack(i + 1)

            sub_set.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return power_set