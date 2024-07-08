class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        min_speed = high
        while low <= high:
            speed = (low + high) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / speed)
            
            if time <= h:
                min_speed = speed
                high = speed - 1
            else:
                low = speed + 1
        return min_speed
        
        