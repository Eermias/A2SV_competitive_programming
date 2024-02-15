class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prev = {0:1}
        count = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            diff = summ - goal
            if diff in prev:
                count += prev[diff]
            prev[summ] = 1 + prev.get(summ, 0)
        
        return count