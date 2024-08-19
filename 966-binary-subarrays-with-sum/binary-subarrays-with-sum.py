class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        summ = 0
        count = 0
        for n in nums:
            summ += n
            remove = summ - goal
            count += prefix[remove]
            prefix[summ] += 1
        
        return count
