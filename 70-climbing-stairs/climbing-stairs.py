class Solution:
    def climbStairs(self, n: int) -> int:
        curr, one, two = 1, 0, 0
        for i in range(n):
            one += curr
            two += curr

            curr = one
            one = two
            two = 0
        
        return curr