class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        for i in range(n - 1):
            temp = curr
            curr += prev
            prev = temp
        
        return curr
        

        