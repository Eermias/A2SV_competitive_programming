class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashed = {}
        for i in range(len(nums)):
            hashed[nums[i]] = 1 + hashed.get(nums[i], 0)
        
        subHash = {}
        l = 0
        complete = 0

        for r in range(len(nums)):
            subHash[nums[r]] = 1 + subHash.get(nums[r], 0)
            while len(subHash) == len(hashed) and l<=r:
                if subHash[nums[l]] == 1:
                    subHash.pop(nums[l])
                else:
                    subHash[nums[l]] -= 1
                l+=1
                complete += len(nums) - r
        return complete
        
        