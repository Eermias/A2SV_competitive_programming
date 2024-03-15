class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        hmax = 0
        l, r = 0, len(citations) - 1
        while l <= r:
            m = (l + r) // 2
            """if n - m > hmax and citations[m] > hmax:
                hmax = min(n - m, citations[m])
                l = m + 1
            else:
                r = m - 1"""
            hmax = max(hmax, min(citations[m], n - m))
            if n - m >= citations[m]:
                #hmax = max(hmax, citations[m])
                l = m + 1
            else:
                #hmax = max(hmax, n - m)
                r = m - 1
            
        
        return hmax
        