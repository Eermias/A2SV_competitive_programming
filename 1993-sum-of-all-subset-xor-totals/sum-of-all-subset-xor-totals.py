class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(i, curr):
            nonlocal total
            if i == len(nums):
                total += curr
                return
            
            #pick or skip respectively
            backtrack(i + 1, curr ^ nums[i])
            backtrack(i + 1, curr)
        
        backtrack(0, 0)
        return total