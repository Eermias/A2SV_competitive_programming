class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        currRow = [1]
        for i in range(len(prevRow) - 1):
            currRow.append(prevRow[i] + prevRow[i + 1])
        currRow.append(1)
        return currRow
        