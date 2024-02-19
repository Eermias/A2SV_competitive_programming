class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            stack.append(nums[i])
        j = len(nums) - 1
        while j >= 0:
            if not stack:
                res[j] = -1
            elif stack and stack[-1] > nums[j]:
                res[j] = stack[-1]
            elif stack and stack[-1] <= nums[j]:
                while stack and stack[-1] <= nums[j]:
                    stack.pop()
                if not stack:
                    res[j] = -1
                else:
                    res[j] = stack[-1]
            stack.append(nums[j])
            j -= 1
        return res




        