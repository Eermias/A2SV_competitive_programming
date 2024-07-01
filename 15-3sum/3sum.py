class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        i = 0
        while i < len(nums):
            a = nums[i]
            l, r = i + 1, len(nums) - 1
            target = 0 - a
            while l < r:
                if nums[l] + nums[r] == target:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return output
