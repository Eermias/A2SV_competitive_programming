class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        l = 0
        while l < len(nums):
            if nums[l] == 0:
                r = l + 1
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r == len(nums):
                    break
                nums[l] = nums[r]
                nums[r] = 0
            l += 1

        return nums
        