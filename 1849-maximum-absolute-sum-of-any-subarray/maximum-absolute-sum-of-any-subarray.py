class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        result = 0

        # find maximum positive window
        curr = 0
        for num in nums:
            curr += num
            result = max(result, curr)
            if curr < 0:
                curr = 0
        
        # find maximum negative window
        curr = 0
        for num in nums:
            curr += num
            result = max(result, abs(curr))
            if curr > 0:
                curr = 0
        
        return result