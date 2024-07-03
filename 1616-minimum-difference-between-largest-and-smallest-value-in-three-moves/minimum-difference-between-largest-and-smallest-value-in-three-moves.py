class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        
        l, r = 3, len(nums) - 1
        res = min(nums[r] - nums[l], 
                  nums[r - 1] - nums[l - 1],
                  nums[r - 2] - nums[l - 2],
                  nums[r - 3] - nums[ l - 3])
        return res