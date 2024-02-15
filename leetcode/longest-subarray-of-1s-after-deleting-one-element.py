class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        zeros = 0
        start = 0
        end = 0

        if 0 not in nums:
            return len(nums)-1

        for i in range(len(nums)):
            if nums[i] != 1:
                start += 1
            else: 
                break
        end = start

        while end < len(nums):
            if zeros < 2:
                if nums[end] == 0:
                    zeros += 1
                longest = max(longest, end-start+1-zeros)
                end += 1
            else:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
        return longest