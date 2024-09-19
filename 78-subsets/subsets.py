class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        curr_set = []
        def backtrack(i):
            if i == len(nums):
                power_set.append(curr_set[:])
                return
            
            curr_set.append(nums[i])
            backtrack(i + 1)

            curr_set.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return power_set
