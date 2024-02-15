class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            diff = summ - k
            if diff in prefix_sum:
                count += prefix_sum[diff]
            prefix_sum[summ] = 1 + prefix_sum.get(summ, 0)
        return count