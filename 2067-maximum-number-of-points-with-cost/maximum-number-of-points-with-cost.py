class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        for r in range(rows):
            if r > 0:
                for i in range(cols):
                    points[r][i] += points[r - 1][i]

            for i in range(cols - 2, -1, -1):
                points[r][i] = max(points[r][i], points[r][i + 1] - 1)
            
            for i in range(1, cols):
                points[r][i] = max(points[r][i], points[r][i - 1] - 1)
            
        return max(points[-1])


