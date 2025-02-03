class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
        longest = max(longest, curr)

        curr = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
        
        return max(longest, curr)

