class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = defaultdict(list)
        for val in nums:
            num = val
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            digit_sum[total].append(val)
        
        ans = -1
        for key, vals in digit_sum.items():
            if len(vals) > 1:
                vals.sort()
                ans = max(ans, vals[-1] + vals[-2])
        
        return ans
        
        