class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total, zeros, negatives = 0, 0, 0
        minn = float('inf')

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                total += abs(matrix[r][c])
                minn = min(minn, abs(matrix[r][c]))

                if matrix[r][c] == 0:
                    zeros += 1
                elif matrix[r][c] < 0:
                    negatives += 1
        
        if zeros or negatives % 2 == 0:
            return total
        return total - 2 * minn