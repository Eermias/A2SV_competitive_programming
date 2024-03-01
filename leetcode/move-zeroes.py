class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            if r == len(nums) - 1:
                for k in range(l,len(nums)):
                    nums[k] = 0
        #return l+2
        #for l in range(len(nums)):
         #   nums[l] = 0
        #return nums