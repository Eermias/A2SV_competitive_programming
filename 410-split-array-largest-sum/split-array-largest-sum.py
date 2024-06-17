class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_max_sum = sum(nums)
        low, high = max(nums), sum(nums)
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            temp_max = 0
            temp_sum = 0
            for n in nums:
                if temp_sum + n <= mid:
                    temp_sum += n
                else:
                    temp_max = max(temp_max, temp_sum)
                    temp_sum = n
                    count += 1
            count += 1
            temp_max = max(temp_max, temp_sum)
            
            if count > k:
                low = mid + 1
            else:
                min_max_sum = min(min_max_sum, temp_max)
                high = mid - 1
        
        return min_max_sum 