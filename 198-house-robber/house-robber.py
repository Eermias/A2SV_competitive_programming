class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)):
            temp = max(curr, prev + nums[i])
            prev = curr
            curr = temp
        
        return curr
