class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def binary_search(i, j):
            l, r = j + 1, len(nums) - 1
            k = j
            while l <= r:
                m = (l + r) // 2
                if nums[m] < nums[i] + nums[j]:
                    k = m
                    l = m + 1
                else:
                    r = m - 1
            return k
            
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                k = binary_search(i, j)
                count += k - j
        return count