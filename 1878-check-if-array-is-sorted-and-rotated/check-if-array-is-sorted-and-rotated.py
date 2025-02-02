class Solution:
    def check(self, nums: List[int]) -> bool:

        idx = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break

    
        original = nums[idx:] + nums[:idx]
        return idx == -1 or sorted(original) == original