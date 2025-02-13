class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        count = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            x, y = min(x, y), max(x, y)
            heappush(nums, 2 * x + y)
            count += 1
        
        return count
