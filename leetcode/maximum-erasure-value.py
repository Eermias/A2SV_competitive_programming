class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        l = 0
        r = 0
        maxSum = float("-inf")
        curr_sum = 0
        while r < len(nums):
            if nums[r] not in visited:
                curr_sum += nums[r]
                visited.add(nums[r])
                r += 1
            else:
                maxSum = max(maxSum, curr_sum)
                while nums[r] in visited:
                    visited.remove(nums[l])
                    curr_sum -= nums[l]
                    l += 1
        maxSum = max(maxSum, curr_sum)
        return maxSum
                

        