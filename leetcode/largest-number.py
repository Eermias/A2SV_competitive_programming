class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = []
        for n in nums:
            arr.append(str(n))

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] < arr[j] + arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

        ans = "".join(arr)
        return "0" if int(ans) == 0 else ans
        
