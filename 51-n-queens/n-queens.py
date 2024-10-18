class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        diagonals = [set(), set()]
        cols = set()

        curr = [['.'] * n for _ in range(n)]
        def backtrack(row):
            if row == n:
                to_string = [''.join(arr) for arr in curr]
                result.append(to_string)
                return
            
            for col in range(n):
                if col not in cols and row + col not in diagonals[0] and row - col not in diagonals[1]:
                    cols.add(col)
                    diagonals[0].add(row + col)
                    diagonals[1].add(row - col)
                    curr[row][col] = 'Q'
                    
                    backtrack(row + 1)

                    cols.remove(col)
                    diagonals[0].remove(row + col)
                    diagonals[1].remove(row - col)
                    curr[row][col] = '.'
        
        backtrack(0)
        return result
        