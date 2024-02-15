class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        maxx = len(arr)
        surplus = 0
        mapp = {}
        for num in arr:
            mapp[num] = 1 + mapp.get(num, 0)
            if num > maxx:
                surplus += 1
        #print(mapp, maxx, surplus)
        for i in range(len(arr), 0, -1):
            if i not in mapp: #O(1)
                if surplus > 0:
                    surplus -= 1
                else:
                    #if maxx - i >= 2:
                        #surplus += 1
                    maxx -= 1
                    print(i, maxx)
            else:
                surplus += mapp[i] - 1
        return maxx

                
        
        
        