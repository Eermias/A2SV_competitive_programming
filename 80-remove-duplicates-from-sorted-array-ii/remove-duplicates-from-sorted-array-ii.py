class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        for r in range(2, len(nums)):
            if l < len(nums):
                nums[l] = nums[r]
                nums[r] = ''
                if nums[l] == nums[l - 2]:
                    nums[l] = ''
                else:
                    l += 1
            elif nums[r] == nums[r - 2]:
                nums[r] = ''
                l = r
        return l
            
            
