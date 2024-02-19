class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = {key:0 for key in range(n)}
        col = {key:0 for key in range(n)}
        for r in range(n):
            for c in range(n):
                row[r] = max(row[r], grid[r][c])
                col[c] = max(col[c], grid[r][c])
        
        increase = 0
        for r in range(n):
            for c in range(n):
                increase += min(row[r], col[c]) - grid[r][c]
        return increase
        
        