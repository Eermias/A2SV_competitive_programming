class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        transpose = [[] for _ in range(col)]
        for row_idx in range(row):
            for col_idx in range(col):
                transpose[col_idx].append(matrix[row_idx][col_idx])

        return transpose
        