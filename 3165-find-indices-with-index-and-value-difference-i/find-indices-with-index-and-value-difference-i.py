class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j - i >= indexDifference and abs(nums[j] - nums[i]) >= valueDifference:
                    return [i, j]
                    
        return [-1, -1]