class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        matrix = deque([deque(row) for row in matrix])

        while matrix:
            top = matrix.popleft()
            while top:
                spiral.append(top.popleft())
            
            while matrix and not matrix[0]:
                matrix.popleft()

            for row in matrix:
                spiral.append(row.pop())
            
            while matrix and not matrix[-1]:
                matrix.pop()

            if matrix:
                bot = matrix.pop()
                while bot:
                    spiral.append(bot.pop())
                
            for col in range(len(matrix) - 1, -1, -1):
                spiral.append(matrix[col].popleft())
        
        return spiral

        