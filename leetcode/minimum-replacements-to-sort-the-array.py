class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        partitions = 0
        lastSorted = nums[-1]
        for i in range(-2, -(len(nums) + 1), -1):
            if nums[i] > lastSorted:
                mod = nums[i] % lastSorted
                if mod == 0:
                    partitions += nums[i]//lastSorted - 1
                else:
                    quot = nums[i]//lastSorted
                    lastSorted = (nums[i])//(quot + 1)
                    partitions += quot
            else:
                lastSorted = nums[i]
        return partitions
                    
        