class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        sortedd = [(nums[i], i) for i in range(len(nums))]
        sortedd.sort(reverse = True)

        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while sortedd and sortedd[-1][0] <= nums[j]:
                val, idx = sortedd.pop()
                max_width = max(max_width, j - idx)
        
        return max_width
