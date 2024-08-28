class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = defaultdict(int)
        for arr in arrays:
            minn[arr[0]] += 1
        
        mins = list(minn.keys())
        mins.sort()
        min1 = mins[0]
        if minn[mins[0]] > 1:
            min2 = mins[0]
        else:
            min2 = mins[1]
        
        max_dis = 0
        for arr in arrays:
            right = arr[-1]
            if arr[0] != min1:
                max_dis = max(max_dis, right - min1)
            else:
                max_dis = max(max_dis, right - min2)
        
        return max_dis