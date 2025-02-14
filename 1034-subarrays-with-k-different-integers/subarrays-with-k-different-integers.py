class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        less = {}
        l = 0
        k_minus = 0
        for r in range(n):
            less[nums[r]] = 1 + less.get(nums[r], 0)
            while len(less) > k - 1:
                less[nums[l]] -= 1
                if less[nums[l]] == 0:
                    less.pop(nums[l])
                l += 1
            k_minus += r - l + 1

        equal = {}
        l = 0
        kk = 0
        for r in range(n):
            equal[nums[r]] = 1 + equal.get(nums[r], 0)
            while len(equal) > k:
                equal[nums[l]] -= 1
                if equal[nums[l]] == 0:
                    equal.pop(nums[l])
                l += 1
            kk += r - l + 1
            

        return kk - k_minus
            