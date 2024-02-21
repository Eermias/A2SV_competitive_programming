class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fine = -1
        for i in range(len(nums)):
            fine = max(fine, i + (nums[i] - 1))
            print(fine)
            if nums[i] == 0 and i != len(nums) - 1:
                if fine < i:
                    return False
        return True
        