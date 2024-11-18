class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev = [0] * cols
        for r in range(rows):
            for i in range(cols):
                points[r][i] += prev[i]

            left = points[r].copy()
            for i in range(cols - 2, -1, -1):
                left[i] = max(left[i], left[i + 1] - 1)
            
            right = points[r].copy()
            for i in range(1, cols):
                right[i] = max(right[i], right[i - 1] - 1)
            
            for i in range(cols):
                points[r][i] = max(left[i], right[i])
                
            prev = points[r].copy()
        
        print(points)
        return max(prev)


