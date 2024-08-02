class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row1, col1 = False, False
        for r in range(ROWS):
            if matrix[r][0] == 0:
                col1 = True
        
        for c in range(COLS):
            if matrix[0][c] == 0:
                row1 = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if row1:
            for c in range(COLS):
                matrix[0][c] = 0
            
        if col1:
            for r in range(ROWS):
                matrix[r][0] = 0
