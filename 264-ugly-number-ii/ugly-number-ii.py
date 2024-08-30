class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n - 1):
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_ugly)

            if ugly[i2] * 2 == next_ugly:
                i2 += 1
            if ugly[i3] * 3 == next_ugly:
                i3 += 1
            if ugly[i5] * 5 == next_ugly:
                i5 += 1
        
        #print(ugly)
        return ugly[-1]
        

            
