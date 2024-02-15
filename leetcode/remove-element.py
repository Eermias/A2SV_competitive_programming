class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        removed = []
        for i in range(len(nums)):
            if nums[i] != val:
                removed.append(nums[i])
        for i in range(len(nums)):
            if i < len(removed):
                nums[i] = removed[i]
            else:
                nums[i] = "_"      
        
        return len(removed)