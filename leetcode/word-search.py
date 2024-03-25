class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(row, col, i, curr):
            if curr == word:
                return True
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or 
                (row, col) in path or word[i] != board[row][col]):
                return False
            
            curr += board[row][col]
            path.add((row, col))

            left = dfs(row, col - 1, i + 1, curr)
            right = dfs(row, col + 1, i + 1, curr)
            up = dfs(row - 1, col, i + 1, curr)
            down = dfs(row + 1, col, i + 1, curr)

            path.remove((row, col))
            return left or right or up or down
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0, ""):
                    return True
        
        return False
        


        

        