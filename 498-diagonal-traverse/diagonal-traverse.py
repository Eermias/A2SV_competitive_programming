class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])

        def goup(r, c):
            if r + 1 < row:
                return (r + 1, c)
            return (r, c + 1)
        
        def godown(r, c):
            if c + 1 < col:
                return (r, c + 1)
            return (r + 1, c)
        
        up = True
        result = []
        r, c = 0, 0
        while len(result) < row * col:
            if up:
                while -1 < r < row and -1 < c < col:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
                r, c = godown(r + 1, c - 1)
                up = False
            else:
                while -1 < r < row and -1 < c < col:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
                r, c = goup(r - 1, c + 1)
                up = True
        
        return result
