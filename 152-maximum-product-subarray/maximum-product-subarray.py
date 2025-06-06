class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        last_neg = 0 if nums[0] >= 0 else nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                last_neg = 0
                continue

            if nums[i - 1]:
                nums[i] *= nums[i - 1]
            ans = max(ans, nums[i])
            if nums[i] < 0:
                if not last_neg:
                    last_neg = nums[i]
                else:
                    ans = max(nums[i] // last_neg, ans)
        
        return ans
