import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from_origin = []
        for point in points:
            distance = math.sqrt(point[0] * point[0] + point[1] * point[1])
            from_origin.append([distance, point])

        from_origin.sort()
        res = []
        for i in range(k):
            res.append(from_origin[i][1])

        return res

        