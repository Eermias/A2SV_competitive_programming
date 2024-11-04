class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        matrix = deque(matrix)

        while matrix:
            top = matrix.popleft()
            top = top[::-1]
            while top:
                spiral.append(top.pop())

            for row in matrix:
                spiral.append(row.pop())
            
            while matrix and not matrix[-1]:
                matrix.pop()
            
            if matrix:
                bot = matrix.pop()
                while bot:
                    spiral.append(bot.pop())
            

            for i in range(len(matrix) - 1, -1, -1):
                matrix[i] = matrix[i][::-1]
                spiral.append(matrix[i].pop())
                matrix[i] = matrix[i][::-1]
            
            while matrix and not matrix[-1]:
                matrix.pop()
        
        return spiral

        