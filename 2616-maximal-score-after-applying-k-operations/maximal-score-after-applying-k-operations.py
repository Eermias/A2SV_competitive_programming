class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        score = 0
        for _ in range(k):
            maxx = heapq.heappop(nums)
            score -= maxx
            heapq.heappush(nums, -((-maxx + 2) // 3))
        
        return score