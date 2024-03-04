class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        row = len(mat)
        col = row
        for row_idx in range(row):
            for col_idx in range(col):
                if row_idx == col_idx or row_idx + col_idx == row - 1:
                    summ += mat[row_idx][col_idx]

        return summ