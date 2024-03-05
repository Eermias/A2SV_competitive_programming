class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and (c, r) not in visited:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                visited.add((r, c))
        
        for row_idx in range(row):
            l, r = 0, col - 1
            while l < r:
                matrix[row_idx][l], matrix[row_idx][r] = matrix[row_idx][r], matrix[row_idx][l]
                l += 1
                r -= 1
        

        