class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #The answer will be true if min(x0, x1, ... xj-1) < xj < max(xj+1, ... xn)
        #finding the minPrefix
        minPrefix = []
        prefix = float("inf")
        for i in range(len(nums)):
            if nums[i] < prefix:
                prefix = nums[i]
            minPrefix.append(prefix)

        #finding the maxSuffix
        maxSuffix = [0 for _ in range(len(nums))]
        suffix = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > suffix:
                suffix = nums[i]
            maxSuffix[i] = suffix
        print(minPrefix)
        print(nums)
        print(maxSuffix)

        #checking for triplet subsequnces: 
        #i.e check for the existence of integer j such that minPrefix[j - 1] < nums[j] < maxSuffix[j + 1]
        for j in range(1, len(nums) - 1):
            if minPrefix[j - 1] < nums[j] < maxSuffix[j + 1]:
                return True
        
        return False

