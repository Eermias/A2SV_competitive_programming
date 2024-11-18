class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        for r in range(rows):
            if r > 0:
                for i in range(cols):
                    points[r][i] += points[r - 1][i]

            left = points[r].copy()
            for i in range(cols - 2, -1, -1):
                left[i] = max(left[i], left[i + 1] - 1)
            
            right = points[r].copy()
            for i in range(1, cols):
                right[i] = max(right[i], right[i - 1] - 1)
            
            for i in range(cols):
                points[r][i] = max(left[i], right[i])
        
        return max(points[-1])


