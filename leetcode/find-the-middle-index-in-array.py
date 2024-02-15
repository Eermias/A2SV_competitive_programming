class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        prefix = 0
        suffix = total
        for i in range(len(nums)):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
        return -1
        