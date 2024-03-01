class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapp = {}
        for n in arr2:
            mapp[n] = 1
        leftPart = []
        rightPart = []
        for n in arr1:
            if n in mapp:
                mapp[n] += 1
            else:
                rightPart.append(n)
        for n in arr2:
            dup = [n] * (mapp[n] - 1)
            leftPart += dup
        rightPart.sort()
        
        return leftPart + rightPart
        
        