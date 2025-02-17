class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        left_sum = 0
        for i in range(len(nums)):
            right_sum = nums[-1] - nums[i]

            if left_sum == right_sum:
                return i
            
            left_sum = nums[i]
        
        return -1