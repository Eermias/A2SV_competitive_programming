class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for i in range(1, len(nums)):
            left_sum = nums[i - 1]
            right_sum = nums[-1] - nums[i]

            if left_sum == right_sum:
                return i - 1
            
            left_sum = nums[i]
        
        return -1