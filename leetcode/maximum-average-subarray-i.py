class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        summ = 0
        l, r = 0, k - 1
        for i in range(k):
            summ += nums[i]
        maxAverage = float(summ)/k
        while r < len(nums) - 1:
            summ -= nums[l]
            l += 1
            r += 1
            summ += nums[r] if r < len(nums) else 0
            maxAverage = max(maxAverage, float(summ)/k)
        return maxAverage

