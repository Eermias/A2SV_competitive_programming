class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                arr[i] = 1
            else:
                if arr[i] - arr[i - 1] >= 2:
                    arr[i] -= (arr[i] - arr[i - 1] - 1)
        return arr[-1]
        