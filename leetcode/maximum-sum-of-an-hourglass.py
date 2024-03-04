class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        grid = [[0 for _ in range(col)]] + grid
        for i in range(row + 1):
            grid[i] = [0] + grid[i]

        #copy:
        prefix = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                prefix[r][c] = grid[r][c] 

        #prefix
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                prefix[r][c] = prefix[r][c] + prefix[r][c - 1] + prefix[r - 1][c] - prefix[r - 1][c - 1]
        
        #calculate each hourglass
        max_hourglass = float("-inf")
        for r in range(1, row - 1):
            for c in range(1, col - 1):
                add = prefix[r + 2][c + 2] - prefix[r - 1][c + 2] - prefix[r + 2][c - 1] + prefix[r - 1][c - 1]
                subtract = grid[r + 1][c] + grid[r + 1][c + 2]
                hourglass = add - subtract
                max_hourglass = max(max_hourglass, hourglass)
        print(grid) 
        print(prefix)      
        return max_hourglass
        
        