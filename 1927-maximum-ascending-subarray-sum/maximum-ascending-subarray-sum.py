class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
        
        return max(max_sum, curr_sum)