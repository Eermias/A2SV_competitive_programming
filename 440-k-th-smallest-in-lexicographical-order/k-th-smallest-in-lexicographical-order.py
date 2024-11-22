class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(curr):
            res = 0
            ngbr = curr + 1
            while curr <= n:
                res += min(ngbr, n + 1) - curr
                curr *= 10
                ngbr *= 10
            
            return res
        
        curr = 1
        i = 1
        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1
        
        return curr