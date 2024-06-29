class Solution(object):
    def isValidSudoku(self, board):
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    n = board[r][c]
                    if n in cols[c] or n in rows[r] or n in sub_boxes[r // 3][c // 3]:
                        return False
                    cols[c].add(n)
                    rows[r].add(n)
                    sub_boxes[r // 3][c // 3].add(n)
        
        return True