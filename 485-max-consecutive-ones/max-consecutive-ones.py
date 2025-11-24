class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                maxx = max(maxx, r - l)
            else:
                l = r = r + 1
        
        return maxx