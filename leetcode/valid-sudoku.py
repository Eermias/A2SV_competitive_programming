class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check for valid rows
        for row in board:
            count = []
            for num in row:
                if num == ".":
                    continue
                else:
                    if num in count:
                        return False
                    count.append(num)

        #check for valid columns
        for row in range(9):
            count = []
            for col in range(9):
                if board[col][row] == ".":
                    continue
                else:
                    if board[col][row] in count:
                        return False
                    count.append(board[col][row])
        
        #check for valid 3x3s
        rowStart = 0
        rowEnd =3
        
        #count = []
        for j in range(3):
            colStart =0
            colEnd =3
            for i in range(3):
                count = []
                for row in range(rowStart,rowEnd):
                    for col in range(colStart,colEnd):
                        if board[col][row] == ".":
                            continue
                        else:
                            if board[col][row] in count:
                                return False
                            count.append(board[col][row])
                colStart += 3
                colEnd +=3
            rowStart += 3
            rowEnd += 3
        return True