class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        count = 0

        for col_idx in range(col):
            for row_idx in range(1, row):
                if strs[row_idx][col_idx] < strs[row_idx - 1][col_idx]:
                    count += 1
                    break
        
        return count
        