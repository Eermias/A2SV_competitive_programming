class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums) + 1
        min_divisor = high
        while low <= high:
            divisor = (low + high) // 2
            total = 0
            for n in nums:
                total += ceil(n / divisor)
            
            if total <= threshold:
                min_divisor = divisor
                high = divisor - 1
            elif total > threshold:
                low = divisor + 1
        
        return min_divisor
    