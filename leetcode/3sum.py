class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            target = -nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == target:
                    currentTriplet = [nums[i],nums[right],nums[left]]
                    if currentTriplet not in triplets:
                        triplets.append(currentTriplet)
                    left += 1
                    right -= 1
                elif currentSum > target:
                    right -= 1
                else:
                    left += 1

        return triplets



