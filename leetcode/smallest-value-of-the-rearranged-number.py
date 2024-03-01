class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        arr = []
        temp = abs(num)
        while temp != 0:
            mod = temp % 10
            arr.append(mod)
            temp = temp // 10

        if num < 0:
            arr.sort(reverse = True)
            res = ""
            for n in arr:
                res += str(n)
            return -1 * int(res)

        else:
            arr.sort()
            for i in range(len(arr)):
                if arr[0] == 0 and arr[i] != 0:
                    arr[0] = arr[i]
                    arr[i] = 0
                    break
            res = ""
            for n in arr:
                res += str(n)
            return int(res)

            

        