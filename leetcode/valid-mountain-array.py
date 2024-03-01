class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
        peak_index = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                peak_index = i
                break
        if not peak_index:
            return False
        right = arr[peak_index + 1:]
        right.sort(reverse = True)
        return right == arr[peak_index + 1:]




        