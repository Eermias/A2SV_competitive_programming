class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0
        r = 1
        for l in range(len(nums) - 1):
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            
            if r == len(nums):
                break
            while r < len(nums) and nums[r] - nums[l] == 1:
                maxx = max(maxx, r - l + 1)
                r += 1
        
        return maxx