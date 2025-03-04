class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        count = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
            else:
                count += (nums[i] + last - 1) // last - 1
                last = nums[i] // ((nums[i] + last - 1) // last)
        
        return count

