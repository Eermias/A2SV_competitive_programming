class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #ONE PASS
        l, mid, r = 0, 0, len(nums) - 1
        while(mid <= r):
            if nums[mid] == 0:
                nums[mid] = nums[l]
                nums[l] = 0
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid] = nums[r]
                nums[r] = 2
                r -= 1
        

        #two pass
        l = 0
        r = 1
        while r < len(nums):
            while nums[l] == 0 and l < r:
                l += 1
            if nums[r] == 0:
                nums[r] = nums[l]
                nums[l] = 0
            r += 1
        l = (l+1) if nums[l] == 0 else l
        r = l + 1
        #second pass
        while r < len(nums):
            while nums[l] == 1 and l < r:
                l += 1
            if nums[r] == 1:
                nums[r] = 2
                nums[l] = 1
            r += 1
        
        
        
        