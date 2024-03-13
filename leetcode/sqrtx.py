class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        sqrt_down = 0
        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            else:
                sqrt_down = max(sqrt_down, m)
                l = m + 1
        
        return sqrt_down

        