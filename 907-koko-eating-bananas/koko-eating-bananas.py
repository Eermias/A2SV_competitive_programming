class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        min_speed = high
        while low <= high:
            mid = (low + high) // 2
            time = 0
            for pile in piles:
                time += max(1, (pile + mid - 1) // mid)
            
            if time <= h:
                min_speed = mid
                high = mid - 1
            else:
                low = mid + 1
        return min_speed
        
        