class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            summ += nums[i]
            max_sum = max(max_sum, summ)
            if summ < 0:
                summ = 0
        return max_sum