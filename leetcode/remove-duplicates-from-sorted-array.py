class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] not in nums[:i]:
                result.append(nums[i])
        for i in range(len(nums)):
            if i<len(result):
                nums[i] = result[i]
            else:
                nums[i] = "_"
        return len(result)