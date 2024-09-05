class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i - 1]
        
        k = k % chalk[-1]
        l, r = 0, len(chalk) - 1
        idx = r
        while l <= r:
            m = (l + r) // 2
            if chalk[m] > k:
                idx = m
                r = m - 1
            else:
                l = m + 1
        
        return idx