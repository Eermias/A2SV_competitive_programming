class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = set(nums)
        if 0 in count:
            return len(count) - 1
        return len(count)