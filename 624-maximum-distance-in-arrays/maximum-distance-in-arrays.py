class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1, min2 = float("inf"), float("inf")
        for array in arrays:
            if array[0] <= min1:
                min2 = min1
                min1 = array[0]
            elif array[0] < min2:
                min2 = array[0]
        
        max_dis = 0
        for arr in arrays:
            right = arr[-1]
            if arr[0] != min1:
                max_dis = max(max_dis, right - min1)
            else:
                max_dis = max(max_dis, right - min2)
        
        return max_dis