class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j - i >= indexDifference and abs(nums[j] - nums[i]) >= valueDifference:
                    ans = [i, j]
                    break
            if ans != [-1, -1]:
                break
        
        return ans