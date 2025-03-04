class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        count = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
            else:
                splits = nums[i] // last
                if nums[i] % last: splits += 1

                count += splits - 1
                last = nums[i] // splits
        
        return count

