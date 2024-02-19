class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = nums[0]
        maxx = nums[0]
        for i in range(1,len(nums)):
            prefix += nums[i]
            if nums[i] > maxx:
                maxx = max(maxx, ceil(prefix/(i + 1)))
        return maxx
            


        