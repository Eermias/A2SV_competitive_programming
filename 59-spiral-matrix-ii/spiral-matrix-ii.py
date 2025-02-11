class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for i in range(n)]
        top, bot, left, right = 0, n - 1, 0, n - 1
        direction = "right"
        i = 1
        while i < n**2 + 1:
            if direction == 'right':
                for c in range(left, right + 1):
                    grid[top][c] = i
                    i += 1
                top += 1
                direction = 'down'
            
            elif direction == 'down':
                for r in range(top, bot + 1):
                    grid[r][right] = i
                    i += 1
                right -= 1
                direction = 'left'
            
            elif direction == 'left':
                for c in range(right, left - 1, -1):
                    grid[bot][c] = i
                    i += 1
                bot -= 1
                direction = 'up'
            
            elif direction == 'up':
                for r in range(bot, top - 1, -1):
                    grid[r][left] = i
                    i += 1
                left += 1
                direction = 'right'
        
        return grid

