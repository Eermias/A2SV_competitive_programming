class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(curr):
            ngbr = curr + 1
            res = 0
            while curr <= n:
                res += min(ngbr, n + 1) - curr
                curr *= 10
                ngbr *= 10
            
            return res
        
        curr = 1
        i = 1
        while i < k:
            nodes = count(curr)
            if i + nodes <= k:
                curr += 1
                i += nodes
            else:
                curr *= 10
                i += 1
        
        return curr
