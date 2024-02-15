class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        zeros = 0
        maxx = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                maxx = max(maxx, r - l)
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if r == len(nums) - 1:
                maxx = max(maxx, r - l + 1)
        return maxx



        