class Solution:
    def check(self, nums: List[int]) -> bool:

        idx = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break


        original = nums[idx:] + nums[:idx] if idx != -1 else nums

        for i in range(1, len(nums)):
            if original[i] < original[i - 1]:
                return False
        return True