class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minn = nums[0]
        for i in range(1, len(nums)):
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()
            
            if stack and stack[-1][0] < nums[i]:
                return True
            stack.append([minn, nums[i]])
            minn =  min(minn, nums[i])
        
        return False
        