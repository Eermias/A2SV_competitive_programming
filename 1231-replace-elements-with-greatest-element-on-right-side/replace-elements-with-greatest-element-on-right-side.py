class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        temp = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = max(arr[i], temp)
            arr[i] = maxx
            maxx = temp
        
        return arr
