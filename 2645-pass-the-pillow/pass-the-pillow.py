class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr = 1
        forward = True
        while time > 0:
            if forward:
                curr += 1
                if curr == n:
                    forward = not forward
            else:
                curr -= 1
                if curr == 1:
                    forward = not forward
            time -= 1
            
        return curr
