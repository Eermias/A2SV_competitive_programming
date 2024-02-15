class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = 0
        for n in nums:
            total += n
        prefix = 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            prefix += nums[i]
            left_sum = (nums[i] * i) - (prefix - nums[i])
            right_sum = (total - prefix) - (nums[i] * (len(nums) - i - 1))
            res[i] = left_sum + right_sum
        return res

               