class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxx_gap = 0
        for i in range(len(nums) - 1):
            maxx_gap = max(maxx_gap, nums[i + 1] - nums[i])
        
        return maxx_gap