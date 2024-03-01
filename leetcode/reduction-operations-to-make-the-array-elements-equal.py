class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        nums.sort(reverse = True)
        largest = 0 #index of largest
        smallest = 0 #index of smallest
        operation = 0
        while smallest < len(nums):
            while smallest < len(nums) and nums[smallest] == nums[largest]:
                smallest += 1
            if smallest < len(nums):
                operation += count[nums[largest]]
                count[nums[smallest]] += count[nums[largest]]
                largest = smallest

        return operation
        
            
            

        
        