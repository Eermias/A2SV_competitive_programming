class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
                
        def rob(start):
            prev, curr = 0, nums[start]
            for i in range(start + 1, len(nums) - (1 - start)):
                temp = max(curr, prev + nums[i])
                prev = curr
                curr = temp
            return curr
        
        return max(rob(0), rob(1))