class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if r == c == 0:
                    continue

                prev = grid[r - 1][c] if r - 1 >= 0 else float('inf')
                if -1 < c - 1:
                    prev = min(prev, grid[r][c - 1])
                
                grid[r][c] += prev
        
        return grid[n - 1][m - 1]
                
