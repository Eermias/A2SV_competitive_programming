class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        i = 0
        ans = 1
        while i < len(nums):
            if nums[i] == maxx:
                count = 1
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    count += 1
                    i += 1
                ans = max(ans, count)
            i += 1
        
        return ans