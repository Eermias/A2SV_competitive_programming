class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxWidth = 0
        for i in range(len(points) - 1):
            maxWidth = max(maxWidth, points[i + 1][0] - points[i][0])
        
        return maxWidth
        