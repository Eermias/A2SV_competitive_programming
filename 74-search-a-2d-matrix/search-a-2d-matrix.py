class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_row(top, bot):
            while top <= bot:
                mid = (top + bot) // 2
                if target > matrix[mid][-1]:
                    top = mid + 1
                elif target < matrix[mid][0]:
                    bot = mid - 1
                else:
                    return mid
            return 0
            
        def get_target(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return True
                elif arr[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
                    
        
        row = get_row(0, len(matrix) - 1)
        if matrix[row][0] <= target <= matrix[row][-1] and get_target(matrix[row]):
            return True
        return False
        