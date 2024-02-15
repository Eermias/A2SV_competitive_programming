class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j] < target:
                    pairs += 1
        return pairs