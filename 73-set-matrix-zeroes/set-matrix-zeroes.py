class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][c] = str(matrix[r][c])
                    matrix[r][0] += "R"
                    matrix[0][c] += "C"
                else:
                    matrix[r][c] = str(matrix[r][c])
    
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if "R" in matrix[r][0] or "C" in matrix[0][c]:
                    matrix[r][c] = 0

        for r in range(1, ROWS):
            if "R" in matrix[r][0]:
                matrix[r][0] = 0
        
        for c in range(1, COLS):
            if "C" in matrix[0][c]:
                matrix[0][c] = 0

        if "R" in matrix[0][0]:
            for c in range(1, COLS):
                matrix[0][c] = 0

        if "C" in matrix[0][0]:
            for r in range(1, ROWS):
                matrix[r][0] = 0

        if "R" in matrix[0][0] or "C" in matrix[0][0]:
            matrix[0][0] = 0

        #print(matrix)
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = int(matrix[r][c])