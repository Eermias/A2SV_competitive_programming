class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minn = len(nums) + 1
        l, r = 0, 0
        summ = 0
        while l <= r and r < len(nums):
            summ += nums[r]
            if summ >= target:
                while summ >= target and l <= r:
                    summ -= nums[l]
                    l += 1
                if l > r:
                    return 1
                else:
                    minn = min(minn, r-l + 2)
            r += 1
        return minn if minn != len(nums) + 1 else 0
        






        