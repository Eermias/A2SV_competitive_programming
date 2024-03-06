class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        copy = arr.copy()
        copy.sort()
        res = []
        for ptrCopy in range(len(copy) - 1, -1, -1):
            ptr = ptrCopy
            while arr[ptr] != copy[ptrCopy]:
                ptr -= 1
            if ptr != ptrCopy:
                res.append(ptr + 1)
                l, r = 0, ptr
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                res.append(ptrCopy + 1)
                l, r = 0, ptrCopy
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
        
        return res


        