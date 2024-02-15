class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = float("inf")
        end = float("-inf")
        for trip in trips:
            start = min(start, trip[1])
            end = max(end, trip[2])
        prefix = [0] * (end - start + 2)
        for trip in trips:
            prefix[trip[1] - start + 1] += trip[0]
            prefix[trip[2] - start + 1] -= trip[0]
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i - 1]
            if prefix[i] > capacity:
                return False
        return True