class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def my_sort(idx):
            l, r = idx, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        index = len(nums) - 2
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        
        if index >= 0:
            other_index = len(nums) - 1
            while other_index > index and nums[index] >= nums[other_index]:
                other_index -= 1
            
            nums[index], nums[other_index] = nums[other_index], nums[index]
            my_sort(index + 1)
        else:
            my_sort(0)
            
        
            



            

        