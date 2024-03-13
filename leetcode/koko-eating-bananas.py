class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSpeed = r
        while l <= r:
            speed = (l + r) // 2
            #print(speed)
            time = 0
            for pile in piles:
                time += ceil(pile / speed)
            if time <= h:
                minSpeed = min(minSpeed, speed)
                r = speed - 1
            else:
                l = speed + 1
            
        return minSpeed
        
        