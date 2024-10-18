class Solution:
    def totalNQueens(self, n: int) -> int:

        diagonals = [set(), set()]
        cols = set()

        def backtrack(row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if col not in cols and row + col not in diagonals[0] and row - col not in diagonals[1]:
                    cols.add(col)
                    diagonals[0].add(row + col)
                    diagonals[1].add(row - col)
                    
                    count += backtrack(row + 1)

                    cols.remove(col)
                    diagonals[0].remove(row + col)
                    diagonals[1].remove(row - col)

            return count

        return backtrack(0)
        