class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #get the row that target could possibly be found
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                break
        
        return False
        