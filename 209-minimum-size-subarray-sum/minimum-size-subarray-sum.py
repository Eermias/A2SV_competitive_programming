class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float("inf")
        window = 0
        l = 0
        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                shortest = min(shortest, r - l + 1)
                window -= nums[l]
                l += 1

        return shortest if shortest != float("inf") else 0