class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mapp = {}
        for i in range(len(intervals)):
            mapp[tuple(intervals[i])] = i
        copy = [[x, y] for x, y in intervals]
        copy.sort()
        res = []
        for interval in intervals:
            l, r = 0, len(intervals) - 1
            right_interval = -1
            while l <= r:
                m = (l + r) // 2
                if copy[m][0] >= interval[1]:
                    right_interval = mapp[tuple(copy[m])]
                    r = m - 1
                else:
                    l = m + 1
            res.append(right_interval)
        
        return res
