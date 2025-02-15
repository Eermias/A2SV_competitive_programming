class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total, negatives = 0, 0
        minn = float('inf')

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                total += abs(matrix[r][c])
                minn = min(minn, abs(matrix[r][c]))

                if matrix[r][c] < 0:
                    negatives += 1
        
        if negatives % 2:
            return total - 2 * minn
        return total